from PyQt6.QtCore import pyqtSignal
from .mqtt_subscriber import MQTTSubscriberThread
import json

class VelocitySubscriberThread(MQTTSubscriberThread):
    velocity_update = pyqtSignal(float, float)  # left, right 

    def __init__(self, mqtt_host, mqtt_port, mqtt_topic="robot/velocity"):
        super().__init__(mqtt_host, mqtt_port, mqtt_topic)

    def on_message(self, client, userdata, msg):
        """Callback khi nhận được message từ MQTT"""
        try:
            message = msg.payload.decode('utf-8')
            #print(f"[MQTT] Received velocity data: {message}")

            data = json.loads(message)
            left = float(data.get('left', 0.0))
            right = float(data.get('right', 0.0))

            self.velocity_update.emit(left, right)

        except (json.JSONDecodeError, ValueError, TypeError) as e:
            print(f"[MQTT] ❌ Error parsing location data: {e}")
