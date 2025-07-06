from PySide6.QtCore import Signal
from .mqtt_subscriber import MQTTSubscriberThread

class AttendanceSubscriberThread(MQTTSubscriberThread):
    attendance_update = Signal(str)  # Signal để gửi giá trị tên về main window

    def __init__(self, mqtt_host="192.168.1.110", mqtt_port=1883, mqtt_topic="robot/attendance"):
        super().__init__(mqtt_host, mqtt_port, mqtt_topic)

    def on_message(self, client, userdata, msg):
        """Callback khi nhận được message"""
        try:
            message = msg.payload.decode('utf-8')
            print(f"Received attendance data: {message}")

            # Giả sử dữ liệu tên là một chuỗi đơn giản hoặc JSON chứa key 'name'
            try:
                import json
                data = json.loads(message)
                if isinstance(data, dict) and 'name' in data:
                    name = str(data['name'])
                else:
                    name = str(message)
            except (json.JSONDecodeError, ValueError):
                name = str(message)

            self.attendance_update.emit(name)

        except (ValueError, TypeError) as e:
            print(f"Error parsing attendance data: {e}")