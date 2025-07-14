import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MQTT.attendance_subscriber import AttendanceSubscriberThread
from base_manager import BaseManager
from mqtt_config import ATTENDANCE_CONFIG

class AttendanceManager(BaseManager):
    def __init__(self, ui, attendance_tab=None):
        super().__init__(ui, AttendanceSubscriberThread, ATTENDANCE_CONFIG)
        
        self.attendance_tab = attendance_tab  # Tham chiếu đến AttendanceTab
        # Khởi tạo giá trị mặc định cho attendance
        self.current_name = "No attendance"
        
    def _connect_signals(self):
        """Kết nối signal cho attendance subscriber"""
        self.subscriber_thread.attendance_update.connect(self.handle_data_update)

    def start_attendance_subscriber(self):
        """Khởi tạo và bắt đầu attendance subscriber thread"""
        self.start_subscriber()

    def stop_attendance_subscriber(self):
        """Dừng attendance subscriber thread"""
        self.stop_subscriber()

    def handle_data_update(self, name, time_str):
        """Cập nhật hiển thị tên người trên UI và cập nhật trạng thái attendance"""
        self.current_name = name
        
        # Cập nhật trạng thái "Present" cho người vừa được nhận diện
        if self.attendance_tab:
            self.attendance_tab.update_status(name=name, status="Present", time=time_str)
            print(f"Attendance updated: {name} - Present at {time_str}")
        else:
            print(f"Attendance received: {name} at {time_str} (No attendance tab connected)")
            
        # Có thể cập nhật thêm label hiển thị tên hiện tại nếu có
        if hasattr(self.ui, 'label_current_person'):
            self.ui.label_current_person.setText(f"Current: {name} ({time_str})")

    def get_current_attendance(self):
        """Trả về tên người hiện tại"""
        return self.current_name

    def clear_attendance(self):
        """Xóa thông tin attendance hiện tại"""
        self.current_name = "No attendance"
        if hasattr(self.ui, 'label_current_person'):
            self.ui.label_current_person.setText(self.current_name)
        print("Attendance cleared")
        
    def set_attendance_tab(self, attendance_tab):
        """Thiết lập tham chiếu đến AttendanceTab"""
        self.attendance_tab = attendance_tab