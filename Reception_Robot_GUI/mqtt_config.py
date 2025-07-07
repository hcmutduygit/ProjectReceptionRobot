"""
MQTT Configuration file
Tập trung quản lý các thông số MQTT để tránh hard-code ở nhiều nơi
"""

class MQTTConfig:
    """Class chứa tất cả cấu hình MQTT"""
    
    # Thông số kết nối MQTT Broker
    MQTT_HOST = "192.168.0.107"
    MQTT_PORT = 1883
    MQTT_KEEPALIVE = 60
    
    # Các MQTT Topics
    TOPICS = {
        "battery": "robot/battery",
        "attendance": "robot/attendance",
        "camera": "robot/camera", 
        "status": "robot/status"
    }
    
    @classmethod
    def get_config(cls, topic_name):
        """
        Lấy cấu hình MQTT cho một topic cụ thể
        
        Args:
            topic_name (str): Tên topic cần lấy config
            
        Returns:
            dict: Dictionary chứa mqtt_host, mqtt_port, mqtt_topic
        """
        if topic_name not in cls.TOPICS:
            raise ValueError(f"Topic '{topic_name}' không tồn tại. Available topics: {list(cls.TOPICS.keys())}")
            
        return {
            "mqtt_host": cls.MQTT_HOST,
            "mqtt_port": cls.MQTT_PORT,
            "mqtt_topic": cls.TOPICS[topic_name]
        }
    
    @classmethod
    def get_all_configs(cls):
        """Lấy tất cả config cho các topic"""
        return {topic: cls.get_config(topic) for topic in cls.TOPICS.keys()}
    
    @classmethod
    def update_host(cls, new_host):
        """Cập nhật MQTT host"""
        cls.MQTT_HOST = new_host
        print(f"MQTT Host updated to: {new_host}")
    
    @classmethod
    def update_port(cls, new_port):
        """Cập nhật MQTT port"""
        cls.MQTT_PORT = new_port
        print(f"MQTT Port updated to: {new_port}")
        
    @classmethod
    def add_topic(cls, topic_name, topic_path):
        """Thêm topic mới"""
        cls.TOPICS[topic_name] = topic_path
        print(f"Added new topic: {topic_name} -> {topic_path}")

# Các default configs cho từng loại manager
BATTERY_CONFIG = MQTTConfig.get_config("battery")
ATTENDANCE_CONFIG = MQTTConfig.get_config("attendance")
