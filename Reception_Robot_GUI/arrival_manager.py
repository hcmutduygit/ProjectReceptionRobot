import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from MQTT.arrival_subscriber import ArrivalSubscriberThread
from base_manager import BaseManager
from mqtt_config import MQTTConfig

ARRIVAL_CONFIG = MQTTConfig.get_config("arrival")

class ArrivalManager(BaseManager):
    def __init__(self, ui):
        super().__init__(ui, ArrivalSubscriberThread, ARRIVAL_CONFIG)
        self.arrival = "false"

    def _connect_signals(self):
        self.subscriber_thread.arrival_update.connect(self.handle_arrival_update)

    def start_arrival_subscriber(self):
        self.start_subscriber()

    def stop_arrival_subscriber(self):
        self.stop_subscriber()

    def handle_arrival_update(self, arrived):
        self.arrival = arrived
        return arrived
        