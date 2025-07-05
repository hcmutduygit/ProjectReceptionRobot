import paho.mqtt.client as mqtt
from PySide6.QtCore import QThread, Signal
import json

class BatterySubscriberThread(QThread):
    battery_update = Signal(int)  # Signal để gửi giá trị battery về main window
    
    def __init__(self, mqtt_host="192.168.1.112", mqtt_port=1883, mqtt_topic="robot/battery"):
        super().__init__()
        self.mqtt_host = mqtt_host
        self.mqtt_port = mqtt_port
        self.mqtt_topic = mqtt_topic
        self.mqtt_keepalive = 60
        self.client = None
        self._stop_requested = False
        
    def on_connect(self, client, userdata, flags, rc):
        """Callback khi kết nối thành công"""
        if rc == 0:
            print(f"Connected to MQTT Broker at {self.mqtt_host}")
            client.subscribe(self.mqtt_topic)
            print(f"Subscribed to topic: {self.mqtt_topic}")
        else:
            print(f"Failed to connect to MQTT Broker. Return code: {rc}")
    
    def on_message(self, client, userdata, msg):
        """Callback khi nhận được message"""
        try:
            # Decode message
            message = msg.payload.decode('utf-8')
            print(f"Received battery data: {message}")
            
            # Thử parse JSON nếu data được gửi dưới dạng JSON
            try:
                data = json.loads(message)
                if isinstance(data, dict) and 'battery' in data:
                    battery_percent = int(data['battery'])
                elif isinstance(data, dict) and 'percentage' in data:
                    battery_percent = int(data['percentage'])
                else:
                    # Nếu không phải JSON object với key mong muốn
                    battery_percent = int(message)
            except (json.JSONDecodeError, ValueError):
                # Nếu không phải JSON, coi như là số nguyên
                battery_percent = int(message)
            
            # Đảm bảo giá trị trong khoảng 0-100
            battery_percent = max(0, min(100, battery_percent))
            
            # Emit signal để cập nhật UI
            self.battery_update.emit(battery_percent)
            
        except (ValueError, TypeError) as e:
            print(f"Error parsing battery data: {e}")
    
    def on_disconnect(self, client, userdata, rc):
        """Callback khi ngắt kết nối"""
        print("Disconnected from MQTT Broker")
    
    def run(self):
        """Main thread execution"""
        try:
            # Khởi tạo MQTT client
            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.on_disconnect = self.on_disconnect
            
            # Kết nối tới broker
            self.client.connect(self.mqtt_host, self.mqtt_port, self.mqtt_keepalive)
            
            # Bắt đầu loop
            while not self._stop_requested:
                self.client.loop(timeout=1.0)
                
        except Exception as e:
            print(f"MQTT Thread error: {e}")
        finally:
            if self.client:
                self.client.disconnect()
    
    def stop(self):
        """Dừng thread"""
        self._stop_requested = True
        if self.client:
            self.client.disconnect()
        self.wait()  # Đợi thread kết thúc
