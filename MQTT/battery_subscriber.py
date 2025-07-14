import json
from PySide6.QtCore import Signal
from .mqtt_subscriber import MQTTSubscriberThread

class BatterySubscriberThread(MQTTSubscriberThread):
    battery_update = Signal(int)  # Signal để gửi giá trị battery về main window

    def __init__(self, mqtt_host, mqtt_port, mqtt_topic="robot/battery"):
        super().__init__(mqtt_host, mqtt_port, mqtt_topic)

    def on_message(self, client, userdata, msg):
        """Callback khi nhận được message"""
        try:
            message = msg.payload.decode('utf-8')
            print(f"Received battery data: {message}")

            try:
                data = json.loads(message)
                if isinstance(data, dict) and 'battery' in data:
                    battery_percent = int(data['battery'])
                elif isinstance(data, dict) and 'percentage' in data:
                    battery_percent = int(data['percentage'])
                else:
                    battery_percent = int(message)
            except (json.JSONDecodeError, ValueError):
                battery_percent = int(message)

            battery_percent = max(0, min(100, battery_percent))
            self.battery_update.emit(battery_percent)

        except (ValueError, TypeError) as e:
            print(f"Error parsing battery data: {e}")