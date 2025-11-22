import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from MQTT.subscriber_goal import GoalSubscriberThread
from manager.manager_base import BaseManager
from mqtt_config import MQTTConfig

ARRIVAL_CONFIG = MQTTConfig.get_config("goal")

class GoalManager(BaseManager):
    def __init__(self, ui):
        super().__init__(ui, GoalSubscriberThread, ARRIVAL_CONFIG)
        self.goal = None
        self.has_arrived = False  # Flag to control emit signal 

    def _connect_signals(self):
        self.subscriber_thread.goal_update.connect(self.handle_goal_update)

    def start_goal_subscriber(self):
        self.start_subscriber()
        self.has_arrived = False  # Reset flag 

    def stop_goal_subscriber(self):
        self.stop_subscriber()

    def handle_goal_update(self, name):
        if name and not self.has_arrived:
            self.has_arrived = True
            self.goal = name
            self.subscriber_thread.goal_update.emit(name)  # Emit once 
        else:
            self.goal = None 