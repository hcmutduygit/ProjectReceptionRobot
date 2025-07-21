import sys, rclpy, threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

# pyuic6 Robot_UI.ui -o robot_ui.py
from ui.font_configurator import apply_custom_fonts
from ui.login import Ui_Login
from ui.robot import Ui_Form_3
from user import handle_login, handle_signup, handle_logout
from attendance import AttendanceTab
from attendance_manager import AttendanceManager
from battery_manager import BatteryManager
from dataplotting import PlotTab
from location import LocationTab
from camera import CameraTab
from location import MapGuiNode  

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.resize(950, 630)
        apply_custom_fonts(self.ui)

class RobotPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_3()
        self.ui.setupUi(self)
        self.resize(950, 630)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_page = LoginPage()
        self.robot_page = RobotPage()
        self.setCentralWidget(self.login_page)

        # list user
        self.registered_users = [{"username": "admin", "password": "123", "fullname": "Admin User", "phone": "0123456789", "verify": "fablab"}]

        # bien trang thai mqtt
        self.login_page.ui.label_mqtt.setText("disconnected")

        # khoi tao battery 
        self.battery_manager = BatteryManager(self.robot_page.ui)
        self.battery_manager.start_battery_subscriber()

        # khoi tao camera
        self.camera_tab = CameraTab(self.robot_page.ui)

        # khoi tao bieu do 
        self.plot_tab = PlotTab(self.login_page.ui)

        # khoi tao map
        self.location_tab = LocationTab(self.robot_page.ui)

        # khoi tao tab diem danh 
        self.attendance_tab = AttendanceTab(self.robot_page.ui)
        self.attendance_manager = AttendanceManager(self.robot_page.ui, self.attendance_tab)
        self.attendance_manager.start_attendance_subscriber()

        # khoi tao MapGuiNode de xu ly tf2 va odom
        self.map_gui_node = MapGuiNode()
        self.executor = rclpy.executors.MultiThreadedExecutor()
        self.executor.add_node(self.map_gui_node)
        self.ros_thread = threading.Thread(target=self.run_executor, daemon=True)
        self.ros_thread.start()

        # bien trang thai locker
        style = "border-radius: 20px;border: 3px solid rgb(0, 41, 77);"
        ocupied = style + "background-color: red;"
        empty = style + "background-color: green;"
        self.login_page.ui.right_status.setStyleSheet(empty)
        self.login_page.ui.left_status.setStyleSheet(ocupied)

        # set moi vo thi hien cai nao 
        self.login_page.ui.Page.setCurrentWidget(self.login_page.ui.Page_signin)
        self.login_page.ui.Dashboard.setCurrentWidget(self.login_page.ui.Dashboard_signin)

        # gan su kien trang dang nhap 
        self.login_page.ui.Signin_btn_signup.clicked.connect(lambda: self.login_page.ui.Page.setCurrentWidget(self.login_page.ui.Page_signup))
        self.login_page.ui.Signin_btn_signin.clicked.connect(lambda: self.login_page.ui.Page.setCurrentWidget(self.login_page.ui.Page_signin))
        self.login_page.ui.Signin_btn_login.clicked.connect(self._handle_login)
        self.login_page.ui.Signup_btn_signup.clicked.connect(self._handle_signup)

        # gan su kien trang sau dang nhap 
        self.robot_page.ui.comboBox.currentTextChanged.connect(self.handle_page_switch)
        #self.ui.Account__btnlogout.clicked.connect(self._handle_logout)

    def run_executor(self):
        """Chạy executor trong thread riêng"""
        try:
            self.executor.spin()
        except Exception as e:
            print(f"❌ Lỗi trong executor: {e}")

    def _handle_login(self):
        if handle_login(self.login_page.ui, self.registered_users):
            self.setCentralWidget(self.robot_page)
            self.robot_page.ui.stackedWidget.setCurrentWidget(self.robot_page.ui.page_control)

    def _handle_signup(self):
        if handle_signup(self.login_page.ui, self.registered_users):
            self.setCentralWidget(self.login_page)

    def _handle_logout(self):
        handle_logout(self)


    def handle_page_switch(self, text):
        if text == "Control Panel":
            self.robot_page.ui.stackedWidget.setCurrentWidget(self.robot_page.ui.page_control)
        elif text == "Attendance":
            self.robot_page.ui.stackedWidget.setCurrentWidget(self.robot_page.ui.page_attendance)

        
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
    widget.show()
    sys.exit(app.exec())