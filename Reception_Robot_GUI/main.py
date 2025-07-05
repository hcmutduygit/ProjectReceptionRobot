import sys, rclpy

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer

from robot_ui import Ui_MainWindow
# pyside6-uic Robot_UI.ui -o robot_ui.py
# hello

from jetson.camera_publisher import CameraPublisherThread
from camera_subcriber import CameraSubscriberThread
from attendance import AttendanceTab
from battery_subscriber import BatterySubscriberThread

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set the size
        self.resize(950, 630)

        # list user
        self.registered_users = [
    {
        "username": "admin",
        "password": "123",
        "fullname": "Admin User",
        "phone": "0123456789",
        "verify": "fablab"
    }
]
        
        # phan tram pin 
        self.battery_percent = 82 
        self.ui.label_battery.setText(f"{self.battery_percent}%")

        # khoi tao camera
        self.camera_pub_thread = None
        self.camera_sub_thread = None
        
        # khoi tao battery subscriber
        self.battery_sub_thread = None

        # khoi tao tab diem danh
        self.attendance_tab = AttendanceTab(self.ui)

        # set moi vô thi hien cai nao 
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)
        self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)   

        # click sang tab khac thi chuyen trang 
        self.ui.Signin_btn_signup.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signup))
        self.ui.Signin_btn_signin.clicked.connect(lambda: self.ui.Page.setCurrentWidget(self.ui.Page_signin))
        self.ui.Signin_btn_login.clicked.connect(self.handle_login)
        self.ui.Signup_btn_signup.clicked.connect(self.handle_signup)
    
        # click sang tab khac thi chuyen trang 
        self.ui.Main_btn_camera.clicked.connect(lambda: self.switch_to_page(self.ui.Page_Camera))
        self.ui.Main_btn_tracking.clicked.connect(lambda: self.switch_to_page(self.ui.Page_tracking))
        self.ui.Main_btn_attendance.clicked.connect(lambda: self.switch_to_page(self.ui.Page_attendance))
        self.ui.Account__btnlogout.clicked.connect(self.handle_logout)

    def handle_login(self):
        username = self.ui.Signin_username.text()
        password = self.ui.Signin_password.text()

        for user in self.registered_users:
            if user["username"] == username and user["password"] == password:
                self.switch_to_page(self.ui.Page_attendance)  # sang giao diện chính
                self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_main)
                # Bắt đầu battery subscriber sau khi đăng nhập thành công
                self.start_battery_subscriber()
                return
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password")
        
        
    def handle_signup(self):
        fullname = self.ui.Signup_name.text()
        phone    = self.ui.Signup_phone.text()
        username = self.ui.Signup_username.text()
        password = self.ui.Signup_password.text()
        verify   = self.ui.Signup_code.text()

        # da du truong thong tin chua?
        if not all([fullname, phone, username, password, verify]):
            QMessageBox.warning(self, "Sign Up Failed", "Please fill in all fields.")
            return

        # verify code?
        if verify.strip().lower() != "fablab":
            QMessageBox.warning(self, "Sign Up Failed", "Incorrect verification code.")
            return

        # co trung username?
        for user in self.registered_users:
            if user["username"] == username:
                QMessageBox.warning(self, "Sign Up Failed", "Username already exists.")
                return

        # Lưu lại nếu hợp lệ
        self.registered_users.append({
            "fullname": fullname,
            "phone": phone,
            "username": username,
            "password": password,
            "verify": verify
        })

        QMessageBox.information(self, "Success", "Account created successfully!")
        self.ui.Page.setCurrentWidget(self.ui.Page_signin)

    def handle_logout(self):
        # Tạo hộp thoại
        msg = QMessageBox(self)
        msg.setWindowTitle("Confirm Logout")
        msg.setText("Are you sure you want to log out?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setIcon(QMessageBox.Question)
        
        # van chua canh giua duoc, chi dam bao no nam trong frame 
        msg.adjustSize()
        main_rect = self.geometry()
        x = main_rect.x() + (main_rect.width() - msg.width()) // 2
        y = main_rect.y() + (main_rect.height() - msg.height()) // 2
        msg.move(x, y)

        # Hiển thị hộp thoại
        reply = msg.exec()

        if reply == QMessageBox.Yes:
            self.stop_camera()
            self.stop_battery_subscriber()
            self.ui.Page.setCurrentWidget(self.ui.Page_signin)
            self.ui.Dashboard.setCurrentWidget(self.ui.Dashboard_signin)

    
    def switch_to_page(self, page_widget):
        self.ui.Page.setCurrentWidget(page_widget)

        # dung cac process dang chay 
        # self.stop_camera()

        # Bật process phù hợp
        page_handlers = {
            self.ui.Page_Camera: self.start_camera,
            #self.ui.Page_tracking: self.start_tracking,...
        }

        handler = page_handlers.get(page_widget)
        if handler:
            handler()


    def start_camera(self):
        if not hasattr(self, "camera_pub_thread") or self.camera_pub_thread is None:
            self.camera_pub_thread = CameraPublisherThread()
            self.camera_pub_thread.start()

        if not hasattr(self, "camera_sub_thread") or self.camera_sub_thread is None:
            self.camera_sub_thread = CameraSubscriberThread(self.ui.camera_label)
            self.camera_sub_thread.ImageUpdate.connect(self.update_camera_frame)
            self.camera_sub_thread.start()

    def stop_camera(self):
        if self.camera_pub_thread:
            self.camera_pub_thread.stop()
            self.camera_pub_thread = None
        if self.camera_sub_thread:
            self.camera_sub_thread.stop()
            self.camera_sub_thread = None

    def update_camera_frame(self, image):
        if self.ui.Page.currentWidget() == self.ui.Page_Camera:
            self.ui.camera_label.setPixmap(QPixmap.fromImage(image))

    def start_battery_subscriber(self):
        """Khởi tạo và bắt đầu battery subscriber thread"""
        if not hasattr(self, "battery_sub_thread") or self.battery_sub_thread is None:
            self.battery_sub_thread = BatterySubscriberThread(
                mqtt_host="192.168.1.112",  # Thay đổi địa chỉ IP này theo broker của bạn
                mqtt_port=1883,
                mqtt_topic="robot/battery"  # Thay đổi topic này theo topic bạn đang sử dụng
            )
            self.battery_sub_thread.battery_update.connect(self.update_battery_display)
            self.battery_sub_thread.start()
            print("Battery subscriber started")

    def stop_battery_subscriber(self):
        """Dừng battery subscriber thread"""
        if self.battery_sub_thread:
            self.battery_sub_thread.stop()
            self.battery_sub_thread = None
            print("Battery subscriber stopped")

    def update_battery_display(self, battery_percent):
        """Cập nhật hiển thị phần trăm pin trên UI"""
        self.battery_percent = battery_percent
        self.ui.label_battery.setText(f"{battery_percent}%")
        print(f"Battery updated to: {battery_percent}%")

    def closeEvent(self, event):
        self.stop_camera()
        self.stop_battery_subscriber()
        rclpy.shutdown()
        event.accept()  



if __name__ == "__main__":
    rclpy.init()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
