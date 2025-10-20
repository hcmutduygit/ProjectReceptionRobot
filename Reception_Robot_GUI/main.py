import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

from ui.font_configurator import apply_custom_fonts
from ui.style import QMSGBOX_STYLE
from ui.main_ui import Ui_MainWindow
from user import handle_login, handle_signup
from attendance import AttendanceTab
from attendance_manager import AttendanceManager
from battery_manager import BatteryManager
from location_manager import LocationManager 
from velocity_manager import VelocityManager 
from location import LocationTab
from camera import CameraController, CameraTab


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_custom_fonts(self.ui)

        #led control testing 
        self.led1_state = 0 
        self.led2_state = 0 
        self.ui.btn_led1.clicked.connect(self.toggle_led1_state)
        self.ui.btn_led2.clicked.connect(self.toggle_led2_state)

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
        self.ui.mode_select_2.currentTextChanged.connect(self.handle_mode_switch)

        # page_attendance 
        self.attendance_tab = AttendanceTab(self.ui)
        self.attendance_manager = AttendanceManager(self.ui, self.attendance_tab)
        self.attendance_manager.start_attendance_subscriber()

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


    def _handle_login(self):
        success =  handle_login(self.ui, self.registered_users, main_window=self)
        if success:
            self.ui.stackedWidget.setCurrentWidget(self.ui.robot)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_control_2)
            self.admin_camera_tab = CameraTab(self.ui.camera_2, self.shared_browser)
            self.admin_location_tab = LocationTab(self.ui.view_map_2)
            self.location_manager = LocationManager(self.ui)
            self.location_manager.location_tab = self.admin_location_tab
            self.location_manager.start_location_subscriber()

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
            

    def handle_mode_switch(self, text):
        if text == "Manual":
            self.ui.robot_mode_2.setCurrentWidget(self.ui.page_5)   
        elif text == "Auto":
            self.ui.robot_mode_2.setCurrentWidget(self.ui.page_6)

        
    def toggle_led1_state(self):
        # Tăng trạng thái: 0 → 1 → 2 → 0 ...
        self.led1_state = (self.led1_state + 1) % 3

        # Gán màu tương ứng
        if self.led1_state == 0:
            color = "rgb(155, 164, 181)"    #grey 
        elif self.led1_state == 1:
            color = "rgb(215, 19, 19)"      #red 
        elif self.led1_state == 2:
            color = "rgb(28, 121, 71)"      #green 
        # Cập nhật style
        self.ui.btn_led1.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: 20px;
                border: 2px solid rgb(0, 0, 0);
            }}
        """)

    def toggle_led2_state (self):
        self.led2_state = not self.led2_state
        if self.led2_state == 0:
            color = "rgb(155, 164, 181)"    #grey 
        else: 
            color = "white"
        self.ui.btn_led2.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: 20px;
                border: 2px solid rgb(0, 0, 0);
            }}
        """)

    def _shutdown_all_services(self):
        self.battery_manager.stop_battery_subscriber()
        self.attendance_manager.stop_attendance_subscriber()
        self.location_manager.stop_location_subscriber()
        self.velocity_manager.stop_velocity_subscriber() 

    def closeEvent(self, event):
        print("Closinggg...")
        self._shutdown_all_services()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showMaximized()  
    sys.exit(app.exec())