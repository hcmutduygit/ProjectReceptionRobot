import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from MQTT.subscriber_goal import GoalSubscriberThread
from manager.manager_base import BaseManager
from mqtt_config import MQTTConfig

GOAL_CONFIG = MQTTConfig.get_config("goal")

class GoalManager(BaseManager):
    def __init__(self, ui, location_tab=None):
        super().__init__(ui, GoalSubscriberThread, GOAL_CONFIG)
        self.goal = None
        self.location_tab = location_tab

    def _connect_signals(self):
        self.subscriber_thread.goal_update.connect(self.handle_goal_update)

    def start_goal_subscriber(self):
        self.start_subscriber()

    def stop_goal_subscriber(self):
        self.stop_subscriber()

    def handle_goal_update(self, name):
        if name:
            self.goal = name
            self.location_tab.plan_path(name)
        else:
            self.goal = None 