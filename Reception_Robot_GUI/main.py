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
from location_manager import LocationManager 
from dataplotting import PlotTab
from location import LocationTab
from camera import CameraController, CameraTab


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
        self.ui.Signin_btn_guest.clicked.connect(self._handle_guest)
        self.ui.Signin_btn_login.clicked.connect(self._handle_login)
        self.ui.Signup_btn_signup.clicked.connect(self._handle_signup) 

        # gan su kien trang sau dang nhap 
        self.ui.comboBox_2.currentTextChanged.connect(self.handle_page_switch)
        self.ui.logout.clicked.connect(self._handle_logout)
        self.ui.logout_2.clicked.connect(self._handle_logout)

    def run_executor(self):
        """Chạy executor trong thread riêng"""
        try:
            self.executor.spin()
        except Exception as e:
            print(f"❌ Lỗi trong executor: {e}")

    '''def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.windowState() == Qt.WindowState.WindowNoState:
                self.resize(950, 630) 
        super().changeEvent(event)'''

    def _handle_login(self):
        if handle_login(self.ui, self.registered_users):
            self.ui.stackedWidget.setCurrentWidget(self.ui.robot)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_control_2)
            self.admin_camera_tab = CameraTab(self.ui.camera_2, self.shared_browser)
            # 1. Tạo GUI tab
            self.admin_location_tab = LocationTab(self.ui.view_map_2)
            # 2. Khởi tạo manager
            self.location_manager = LocationManager(self.ui)
            # 3. Gán location_tab cho manager
            self.location_manager.location_tab = self.admin_location_tab
            # 4. Start subscriber sau cùng
            self.location_manager.start_location_subscriber()

    def _handle_signup(self):
        if handle_signup(self.ui, self.registered_users):
            self.ui.stackedWidget.setCurrentWidget(self.ui.login)
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)

    def _handle_guest(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.guest)
        self.guest_camera_tab = CameraTab(self.ui.camera_4, self.shared_browser)
        # 1. Tạo GUI tab
        self.guest_location_tab = LocationTab(self.ui.view_map)
        # 2. Khởi tạo manager
        self.location_manager = LocationManager(self.ui)
        # 3. Gán location_tab cho manager
        self.location_manager.location_tab = self.guest_location_tab
        # 4. Start subscriber sau cùng
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
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_telemetry_2)

        
    def _shutdown_all_services(self):
        self.battery_manager.stop_battery_subscriber()
        self.attendance_manager.stop_attendance_subscriber()
        self.location_manager.stop_location_subscriber()

    def closeEvent(self, event):
        print("Đóng cửa sổ, dọn dẹp tài nguyên...")
        self._shutdown_all_services()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.showMaximized()  
    sys.exit(app.exec())