import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MQTT.battery_subscriber import BatterySubscriberThread

class BatteryManager:
    def __init__(self, ui):
        self.ui = ui
        self.battery_sub_thread = None
        # Khởi tạo giá trị mặc định cho battery
        self.battery_percent = 88
        self.ui.label_battery.setText(f"{self.battery_percent}%")
        
    def start_battery_subscriber(self):
        """Khởi tạo và bắt đầu battery subscriber thread"""
        if not hasattr(self, "battery_sub_thread") or self.battery_sub_thread is None:
            self.battery_sub_thread = BatterySubscriberThread(
                mqtt_host="192.168.1.110",  # Thay đổi địa chỉ IP này theo broker của bạn
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
