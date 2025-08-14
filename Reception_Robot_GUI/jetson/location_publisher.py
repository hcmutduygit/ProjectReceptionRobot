#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import sys
import json
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import math

# MQTT Configuration
MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "robot/location"  # Bạn có thể đổi tên topic nếu cần

# Define callback functions for MQTT
def on_connect_old(client, userdata, flags, rc):
    print(f"[MQTT] Connected with result code {rc}")

def on_connect_new(client, userdata, flags, reason_code, properties=None):
    print(f"[MQTT] Connected with reason code {reason_code}")

def on_publish_old(client, userdata, mid):
    print(f"[MQTT] Message published with mid: {mid}")

def on_publish_new(client, userdata, mid, reason_code=None, properties=None):
    print(f"[MQTT] Message published with mid: {mid}")

# Create MQTT client
try:
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect_new
    mqttc.on_publish = on_publish_new
    print("Using paho-mqtt v2 API")
except AttributeError:
    mqttc = mqtt.Client()
    mqttc.on_connect = on_connect_old
    mqttc.on_publish = on_publish_old
    print("Using paho-mqtt v1 API")

mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc.loop_start()

# ROS2 Node
class PoseToMQTT(Node):
    def __init__(self):
        super().__init__('pose_to_mqtt_node')
        self.subscription = self.create_subscription(Odometry, '/odom', self.pose_callback, 10)

    def pose_callback(self, msg: Odometry):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation

        # Convert quaternion to yaw angle (theta)
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        theta = math.degrees(math.atan2(siny_cosp, cosy_cosp))

        payload = {
            "x": round(x, 3),
            "y": round(y, 3),
            #"theta": round(theta, 2)
        }

        try:
            mqttc.publish(MQTT_TOPIC, json.dumps(payload))
            print(f"[ROS2→MQTT] Published: {payload}")
        except Exception as e:
            self.get_logger().error(f"Failed to publish to MQTT: {e}")

def main():
    rclpy.init()
    node = PoseToMQTT()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        node.destroy_node()
        rclpy.shutdown()
        mqttc.loop_stop()
        mqttc.disconnect()

if __name__ == '__main__':
    main()
