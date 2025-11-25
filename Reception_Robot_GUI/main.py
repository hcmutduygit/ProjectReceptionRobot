import os, sys, json
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

from ui.font_configurator import apply_custom_fonts
from ui.style import QMSGBOX_STYLE
from ui.main_ui import Ui_MainWindow
from user import handle_login, handle_signup
from attendance import AttendanceTab

from manager.manager_attendance import AttendanceManager
from manager.manager_battery import BatteryManager
from manager.manager_location import LocationManager 
from manager.manager_arrival import ArrivalManager 
from manager.manager_velocity import VelocityManager 
from manager.manager_telemetry import TelemetryManager
from manager.manager_goal import GoalManager

from location import LocationTab
from camera import CameraController, CameraTab
from robot_telemetry import PlotTelemetry

from MQTT.publisher_goal import GoalPublisher 

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_custom_fonts(self.ui)

        # list user
        self.registered_users = [{"username": "admin", "password": "123", "fullname": "Admin User", "phone": "0123456789", "verify": "fablab"}]

        # thanh trang thai 
        self.battery_manager = BatteryManager(self.ui)
        self.battery_manager.start_battery_subscriber()

        # page_control
        self.camera_controller = CameraController()
        self.shared_browser = self.camera_controller.get_browser()
        self.velocity_manager = VelocityManager(self.ui)
        self.velocity_manager.start_velocity_subscriber()
        self.arrival_manager = ArrivalManager(self.ui)
        self.arrival_manager.start_arrival_subscriber()
        self.ui.mode_select_2.currentTextChanged.connect(self.handle_mode_switch)

        # page_attendance 
        self.attendance_tab = AttendanceTab(self.ui)
        self.attendance_manager = AttendanceManager(self.ui, self.attendance_tab)
        self.attendance_manager.start_attendance_subscriber()

        # page_telemetry
        self.telemetry_tab = PlotTelemetry(self.ui)
        self.telemetry_manager = TelemetryManager(self.ui, self.telemetry_tab)
        self.telemetry_manager.start_telemetry_subscriber()

        # khoi tao 
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)
        self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)

        # gan su kien trang dang nhap 
        self.ui.Signin_btn_signup.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signup))
        self.ui.Signin_btn_signin.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signin))
        self.ui.Signin_btn_guest.clicked.connect(self._handle_guest)
        self.ui.Signin_btn_login.clicked.connect(self._handle_login)
        self.ui.Signup_btn_signup.clicked.connect(self._handle_signup) 

        # gan su kien trang sau dang nhap 
        self.ui.comboBox_2.currentTextChanged.connect(self.handle_page_switch)
        self.ui.logout.clicked.connect(self._handle_logout)
        self.ui.logout_2.clicked.connect(self._handle_logout)
        self.ui.mode_select_2.currentTextChanged.connect(self.handle_mode_switch)



    def _handle_login(self):
        success =  handle_login(self.ui, self.registered_users, main_window=self)
        if success:
            self.ui.stackedWidget.setCurrentWidget(self.ui.robot)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_control_2)
            self.admin_camera_tab = CameraTab(self.ui.camera_2, self.shared_browser)
            self.admin_location_tab = LocationTab(self.ui.view_map_2)
            self.admin_location_tab.logger.cte_signal.connect(self.telemetry_tab.update_cte)
            self.add_path_planning_buttons(self.admin_location_tab)
            self.arrival_manager.subscriber_thread.arrival_update.connect(lambda arrived: self.handle_arrival_signal(arrived))
            self.location_manager = LocationManager(self.ui)
            self.location_manager.location_tab = self.admin_location_tab
            self.location_manager.start_location_subscriber()
            self.goal_manager = GoalManager(self.ui)
            self.goal_manager.location_tab = self.admin_location_tab
            self.goal_manager.start_goal_subscriber()

    def _handle_signup(self):
        success = handle_signup(self.ui, self.registered_users, main_window=self)
        if success:
            self.ui.stackedWidget.setCurrentWidget(self.ui.login)
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)

    def _handle_guest(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.guest)
        self.guest_camera_tab = CameraTab(self.ui.camera_4, self.shared_browser)
        self.guest_location_tab = LocationTab(self.ui.view_map)
        self.add_path_planning_buttons(self.guest_location_tab)
        self.location_manager = LocationManager(self.ui)
        self.location_manager.location_tab = self.guest_location_tab
        self.location_manager.start_location_subscriber()

    def _handle_logout(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("Confirm Logout")
        msgbox.setText("Are you sure you want to log out?")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgbox.setStyleSheet(QMSGBOX_STYLE)
        reply = msgbox.exec()
        if reply == QMessageBox.StandardButton.Yes:
            self._shutdown_all_services()
            self.ui.stackedWidget.setCurrentWidget(self.ui.login)
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)
            self.ui.comboBox_2.setCurrentIndex(0)


    def handle_page_switch(self, text):
        if text == "Control Panel":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_control_2)   
        elif text == "Attendance":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_attendance_2)
        elif text == "Robot Telemetry":
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_data)
            

    def handle_mode_switch(self, text):
        if text == "Manual":
            self.ui.robot_mode_2.setCurrentWidget(self.ui.page_5)   
        elif text == "Auto":
            self.ui.robot_mode_2.setCurrentWidget(self.ui.page_6)
            

    def add_path_planning_buttons(self, location_tab):
        goals = location_tab.get_goal_names()
        buttons = [self.ui.btn_goal_A, self.ui.btn_goal_B, self.ui.btn_goal_C, self.ui.btn_goal_D]

        for btn, name in zip(buttons, goals):
            btn.setText(name)
            btn.clicked.connect(lambda checked=False, n=name: (self.ui.robot_status.setText("Guidance"),
                                                               self.ui.robot_status_2.setText("Guidance"),
                                                               self.ui.robot_mode_2.setCurrentWidget(self.ui.page_log),
                                                               self.ui.label_log.setText(f"Robot is moving to {n}"),
                                                               self.send_goal(n)))

    def send_goal(self, place: str):
        goal_json = json.dumps(place)
        print(f"Goal in /map coordinates (JSON): {goal_json}")
        publisher = GoalPublisher()
        publisher.publish_goal(goal_json)

    def handle_arrival_signal(self, arrived):
        if arrived == 1 and hasattr(self, 'admin_location_tab'):
            self.ui.robot_mode_2.setCurrentWidget(self.ui.page_6)
            self.admin_location_tab.logger.stop_logging()  # Dừng + export
            self.ui.robot_status.setText("Idle")
            self.ui.robot_status_2.setText("Idle")

    def _shutdown_all_services(self):
        self.battery_manager.stop_battery_subscriber()
        self.attendance_manager.stop_attendance_subscriber()
        self.location_manager.stop_location_subscriber()
        self.velocity_manager.stop_velocity_subscriber() 
        self.arrival_manager.stop_arrival_subscriber() 
        self.telemetry_manager.stop_telemetry_subscriber() 
        self.goal_manager.stop_goal_subscriber() 

    def closeEvent(self, event):
        print("Closinggg...")
        self._shutdown_all_services()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showMaximized()  
    sys.exit(app.exec())