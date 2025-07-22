import sys, rclpy, threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt6.QtCore import QSize, Qt, QEvent
from PyQt6.QtGui import QIcon

# pyuic6 Robot_UI.ui -o robot_ui.py
from ui.font_configurator import apply_custom_fonts
from ui.style import QMSGBOX_STYLE
from ui.main_ui import Ui_MainWindow
from user import handle_login, handle_signup
from attendance import AttendanceTab
from attendance_manager import AttendanceManager
from battery_manager import BatteryManager
from dataplotting import PlotTab
from location import LocationTab
from camera import CameraTab
from location import MapGuiNode


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_custom_fonts(self.ui)

        # list user
        self.registered_users = [{"username": "admin", "password": "123", "fullname": "Admin User", "phone": "0123456789", "verify": "fablab"}]

        # thanh trang thai 
        self.ui.label_mqtt.setText("disconnected")
        self.ui.label_mqtt_3.setText("disconnected")
        self.battery_manager = BatteryManager(self.ui)
        self.battery_manager.start_battery_subscriber()

        # page_control
        self.camera_tab = CameraTab(self.ui)
        self.location_tab = LocationTab(self.ui)
        self.map_gui_node = MapGuiNode()
        self.executor = rclpy.executors.MultiThreadedExecutor()
        self.executor.add_node(self.map_gui_node)
        self.ros_thread = threading.Thread(target=self.run_executor, daemon=True)
        self.ros_thread.start()
        style = "border-radius: 20px;border: 3px solid rgb(0, 41, 77);"
        ocupied = style + "background-color: red;"
        empty = style + "background-color: green;"
        self.ui.right_status_2.setStyleSheet(empty)
        self.ui.left_status_2.setStyleSheet(ocupied)

        # page_telemetry  
        self.plot_tab = PlotTab(self.ui)

        # page_attendance 
        self.attendance_tab = AttendanceTab(self.ui)
        self.attendance_manager = AttendanceManager(self.ui, self.attendance_tab)
        self.attendance_manager.start_attendance_subscriber()


        # set moi vo thi hien cai nao 
        self.ui.stackedWidget.setCurrentWidget(self.ui.login)
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)
        self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)

        # gan su kien trang dang nhap 
        self.ui.Signin_btn_signup.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signup))
        self.ui.Signin_btn_signin.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signin))
        self.ui.Signin_btn_login.clicked.connect(self._handle_login)
        self.ui.Signup_btn_signup.clicked.connect(self._handle_signup)

        # gan su kien trang sau dang nhap 
        self.ui.comboBox_2.currentTextChanged.connect(self.handle_page_switch)

    def run_executor(self):
        """Chạy executor trong thread riêng"""
        try:
            self.executor.spin()
        except Exception as e:
            print(f"❌ Lỗi trong executor: {e}")

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.windowState() == Qt.WindowState.WindowNoState:
                self.resize(950, 630)  # 👈 Khi thoát fullscreen thì đặt lại kích thước
        super().changeEvent(event)

    def _handle_login(self):
        if handle_login(self.ui, self.registered_users):
            self.ui.stackedWidget.setCurrentWidget(self.ui.robot)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_control_2)

    def _handle_signup(self):
        if handle_signup(self.ui, self.registered_users):
            self.ui.stackedWidget.setCurrentWidget(self.ui.login)
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)


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
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_telemetry_2)
        elif text == "Logout":
            self._handle_logout()


        
    def _shutdown_all_services(self):
        self.battery_manager.stop_battery_subscriber()
        self.attendance_manager.stop_attendance_subscriber()
        self.executor.shutdown()
        self.map_gui_node.destroy_node()

    def closeEvent(self, event):
        print("Đóng cửa sổ, dọn dẹp tài nguyên...")
        self._shutdown_all_services()
        rclpy.shutdown()
        event.accept()

if __name__ == "__main__":
    rclpy.init()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showMaximized()  
    sys.exit(app.exec())