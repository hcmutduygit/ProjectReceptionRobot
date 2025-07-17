import sys, rclpy

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PyQt6.QtGui import QPixmap, QBrush, QPen
from PyQt6.QtCore import Qt

# pyuic6 Robot_UI.ui -o robot_ui.py

from ui.font_configurator import apply_custom_fonts
from ui.robot_ui import Ui_MainWindow
from user import handle_login, handle_signup, handle_logout
from camera_subcriber import CameraSubscriberThread
from attendance import AttendanceTab
from battery_manager import BatteryManager
from attendance_manager import AttendanceManager
from dataplotting import PlotTab


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(950, 630)
        apply_custom_fonts(self.ui)

        # list user
        self.registered_users = [{"username": "admin","password": "123","fullname": "Admin User","phone": "0123456789","verify": "fablab"}]

        # Tạo scene và gán vào QGraphicsView
        scene = QGraphicsScene()
        pixmap = QPixmap("resources/Map/map.png")  # Ảnh bản đồ
        scene.addPixmap(pixmap)
        self.ui.view_map.setScene(scene)

        # Gợi ý lưu lại để sau này vẽ robot
        self.map_scene = scene
        x, y = 150, 120  # Tọa độ robot trên ảnh
        self.map_scene.addEllipse(x, y, 10, 10, QPen(Qt.GlobalColor.red), QBrush(Qt.GlobalColor.red))


        # bien trang thai mqtt
        self.ui.label_mqtt.setText("disconnected")

        # khoi tao battery 
        self.battery_manager = BatteryManager(self.ui)
        self.battery_manager.start_battery_subscriber()

        # khoi tao camera
        self.camera_sub_thread = None

        # khoi tao bieu do 
        self.plot_tab = PlotTab(self.ui)

        # khoi tao tab diem danh 
        self.attendance_tab = AttendanceTab(self.ui)    # hien giao dien 
        self.attendance_manager = AttendanceManager(self.ui, self.attendance_tab)   # du lieu do manager cap nhat tham chieu den attendance table 
        self.attendance_manager.start_attendance_subscriber()

        
        # bien trang thai locker (mot tao file robot status)
        style = "border-radius: 20px;border: 3px solid rgb(0, 41, 77);"
        ocupied = style + "background-color: red;"
        empty = style + "background-color: green;"
        self.ui.right_status.setStyleSheet(empty)
        self.ui.left_status.setStyleSheet(ocupied)

        # set moi vô thi hien cai nao 
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

    def switch_to_page(self, page_widget):
            self.ui.Page.setCurrentWidget(page_widget)  # chuyen tab 

            # Bật process phù hợp
            page_handlers = {
                self.ui.Page_Camera: self.start_camera,
                #self.ui.Page_tracking: self.start_tracking,...
            }
            handler = page_handlers.get(page_widget)
            if handler:
                handler()


    def _handle_login(self):
        if handle_login(self.ui, self.registered_users):
            self.switch_to_page(self.ui.Page_attendance)  # sang giao diện chính
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_main)        

    def _handle_signup(self):
        if handle_signup(self.ui, self.registered_users):
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)

    def _handle_logout(self):
        handle_logout(self)        
    

    def start_camera(self):
        '''if not hasattr(self, "camera_pub_thread") or self.camera_pub_thread is None:
            self.camera_pub_thread = CameraPublisherThread()
            self.camera_pub_thread.start()'''

        if not hasattr(self, "camera_sub_thread") or self.camera_sub_thread is None:
            self.camera_sub_thread = CameraSubscriberThread(self.ui.camera_label)
            self.camera_sub_thread.ImageUpdate.connect(self.update_camera_frame)
            self.camera_sub_thread.start()

    def stop_camera(self):
        '''if self.camera_pub_thread:
            self.camera_pub_thread.stop()
            self.camera_pub_thread = None'''
        if self.camera_sub_thread:
            self.camera_sub_thread.stop()
            self.camera_sub_thread = None

    def update_camera_frame(self, image):
        if self.ui.Page.currentWidget() == self.ui.Page_Camera:
            self.ui.camera_label.setPixmap(QPixmap.fromImage(image))

    def _shutdown_all_services(self):
        self.stop_camera()
        self.battery_manager.stop_battery_subscriber()
        self.attendance_manager.stop_attendance_subscriber()
        rclpy.shutdown()

    def closeEvent(self, event):
        self._shutdown_all_services()
        event.accept()  


if __name__ == "__main__":
    rclpy.init()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())