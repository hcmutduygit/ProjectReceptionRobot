import sys, rclpy, threading

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap

# pyuic6 Robot_UI.ui -o robot_ui.py
from ui.font_configurator import apply_custom_fonts
from ui.robot_ui import Ui_MainWindow
from user import handle_login, handle_signup, handle_logout
from attendance import AttendanceTab
from attendance_manager import AttendanceManager
from battery_manager import BatteryManager
from dataplotting import PlotTab
from location import LocationTab
from camera import CameraTab
from location import MapGuiNode  # Thêm MapGuiNode từ location

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(950, 630)
        apply_custom_fonts(self.ui)

        # list user
        self.registered_users = [{"username": "admin", "password": "123", "fullname": "Admin User", "phone": "0123456789", "verify": "fablab"}]

        # bien trang thai mqtt
        self.ui.label_mqtt.setText("disconnected")

        # khoi tao battery 
        self.battery_manager = BatteryManager(self.ui)
        self.battery_manager.start_battery_subscriber()

        # khoi tao camera
        self.camera_tab = CameraTab(self.ui)

        # khoi tao bieu do 
        self.plot_tab = PlotTab(self.ui)

        # khoi tao map
        self.location_tab = LocationTab(self.ui)

        # khoi tao tab diem danh 
        self.attendance_tab = AttendanceTab(self.ui)
        self.attendance_manager = AttendanceManager(self.ui, self.attendance_tab)
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
        self.ui.right_status.setStyleSheet(empty)
        self.ui.left_status.setStyleSheet(ocupied)

        # set moi vo thi hien cai nao 
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)
        self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)

        # gan su kien trang dang nhap 
        self.ui.Signin_btn_signup.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signup))
        self.ui.Signin_btn_signin.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signin))
        self.ui.Signin_btn_login.clicked.connect(self._handle_login)
        self.ui.Signup_btn_signup.clicked.connect(self._handle_signup)

        # gan su kien trang sau dang nhap 
        self.ui.Main_btn_camera.clicked.connect(lambda: self.switch_to_page(self.ui.Page_Camera))
        self.ui.Main_btn_tracking.clicked.connect(lambda: self.switch_to_page(self.ui.Page_tracking))
        self.ui.Main_btn_attendance.clicked.connect(lambda: self.switch_to_page(self.ui.Page_attendance))
        self.ui.Main_btn_robotstatus.clicked.connect(lambda: self.switch_to_page(self.ui.Page_robotstatus))
        self.ui.Main_btn_data.clicked.connect(lambda: self.switch_to_page(self.ui.Page_data))
        self.ui.Account__btnlogout.clicked.connect(self._handle_logout)

    def run_executor(self):
        """Chạy executor trong thread riêng"""
        try:
            self.executor.spin()
        except Exception as e:
            print(f"❌ Lỗi trong executor: {e}")

    def switch_to_page(self, page_widget):
        self.ui.Page.setCurrentWidget(page_widget)
        page_handlers = {
            #self.ui.Page_Camera: self.start_camera,
            #self.ui.Page_tracking: self.start_tracking,...
        }
        handler = page_handlers.get(page_widget)
        if handler:
            handler()

    def _handle_login(self):
        if handle_login(self.ui, self.registered_users):
            self.switch_to_page(self.ui.Page_attendance)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_main)

    def _handle_signup(self):
        if handle_signup(self.ui, self.registered_users):
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)

    def _handle_logout(self):
        handle_logout(self)

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