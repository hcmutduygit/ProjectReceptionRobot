import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from MQTT.location_subscriber import LocationSubscriberThread
from base_manager import BaseManager
from mqtt_config import MQTTConfig

LOCATION_CONFIG = MQTTConfig.get_config("location")

class LocationManager(BaseManager):
    def __init__(self, ui, location_tab=None):
        super().__init__(ui, LocationSubscriberThread, LOCATION_CONFIG)
        # Giá trị mặc định ban đầu
        self.location_tab = location_tab
        self.location = {'x': '17.78', 'y': '2.35', 'theta': '??'} 
        self._update_location_labels()

    def _connect_signals(self):
        self.subscriber_thread.location_update.connect(self.handle_data_update)

    def start_location_subscriber(self):
        self.start_subscriber()

    def stop_location_subscriber(self):
        self.stop_subscriber()

    def handle_data_update(self, x, y, theta):
        self.location = {
            'x': f"{x:.2f}",
            'y': f"{y:.2f}",
            'theta': f"{theta:.1f}°"
        }
        self._update_location_labels()
        #print(f"📍Location updated: x={x:.2f}, y={y:.2f}, θ={theta:.1f}°")
        if self.location_tab is not None:
            self.location_tab.set_location(x, y, theta)
        else:
            print("Location_tab chưa được gán.")

    def _update_location_labels(self):
        """Hiển thị vị trí lên các QLabel trong UI"""
        self.ui.label_xy.setText(f"X: {self.location['x']}, Y: {self.location['y']}")
        self.ui.label_xy_2.setText(f"X: {self.location['x']}, Y: {self.location['y']}")
        self.ui.label_xy_3.setText(f"X: {self.location['x']}, Y: {self.location['y']}")
        self.ui.label_theta.setText(f"θ: {self.location['theta']}")
        self.ui.label_theta_2.setText(f"θ: {self.location['theta']}")
        self.ui.label_theta_3.setText(f"θ: {self.location['theta']}")
