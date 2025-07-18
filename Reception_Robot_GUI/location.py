from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer

import math
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from threading import Thread


class MapGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.zoom_factor = 1.25

    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            self.scale(self.zoom_factor, self.zoom_factor)
        else:
            self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)


class ROSNode(Node):
    def __init__(self, update_callback):
        super().__init__('map_gui_listener')
        self.update_callback = update_callback
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

    def odom_callback(self, msg: Odometry):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        # Chuyển quaternion sang yaw
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        theta = math.degrees(math.atan2(siny_cosp, cosy_cosp))
        self.update_callback(x, y, theta)


class LocationTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.map_scene = QGraphicsScene()

        layout = self.ui.view_map.parent().layout()
        self.ui.view_map.setParent(None)

        self.ui.view_map = MapGraphicsView()
        layout.addWidget(self.ui.view_map)
        self.ui.view_map.setScene(self.map_scene)

        self.load_map("Reception_Robot_GUI/resources/Map/map_2.png")

        # Cấu hình map.yaml
        self.map_resolution = 0.05  # mét/pixel
        self.map_origin = (-1.38, -2.4)  # gốc bản đồ (x, y) tính bằng mét

        # Tạo robot
        triangle = QPolygonF([
            QPointF(0, -8),
            QPointF(5, 10),
            QPointF(-5, 10)
        ])
        self.robot_item = QGraphicsPolygonItem(triangle)
        self.robot_item.setBrush(QBrush(QColor(101, 230, 248)))
        self.robot_item.setPen(QPen(Qt.GlobalColor.black, 1))
        self.robot_item.setTransformOriginPoint(0, 0)
        self.map_scene.addItem(self.robot_item)

        # Khởi động ROS node trong luồng riêng
        self.ros_thread = Thread(target=self.start_ros_node, daemon=True)
        self.ros_thread.start()

    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print("❌ Không thể load bản đồ:", path)
            return
        self.map_scene.addPixmap(pixmap)

    def start_ros_node(self):
        if not rclpy.ok():
            rclpy.init()

        self.node = ROSNode(self.update_robot_position)
        rclpy.spin(self.node)


    def update_robot_position(self, x, y, theta):
        """Callback khi nhận được pose mới từ ROS"""
        # Convert tọa độ thực tế (mét) về pixel GUI
        px = (x - self.map_origin[0]) / self.map_resolution
        py = (-(y - self.map_origin[1])) / self.map_resolution  # PyQt y ngược

        def update():
            print (f'updating...')
            self.robot_item.setPos(px, py)
            self.robot_item.setRotation(-theta)

        # Chạy update trong main thread của Qt
        QTimer.singleShot(0, update)
