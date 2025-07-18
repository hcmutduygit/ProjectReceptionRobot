from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer, QRectF

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

        self.map_resolution = 0.05  # mét/pixel
        self.map_origin = (-1.38, -2.4)

        triangle = QPolygonF([
            QPointF(0, -4),
            QPointF(2, 5),
            QPointF(-2, 5)
        ])
        self.robot_item = QGraphicsPolygonItem(triangle)
        self.robot_item.setBrush(QBrush(QColor(101, 230, 248)))
        self.robot_item.setPen(QPen(Qt.GlobalColor.black, 1))
        self.robot_item.setTransformOriginPoint(0, 0)
        self.map_scene.addItem(self.robot_item)

        # ⚠️ Tạm không chạy ROS để test GUI
        # self.ros_thread = Thread(target=self.start_ros_node, daemon=True)
        # self.ros_thread.start()

        # 🔁 Bắt đầu giả lập pose thay đổi
        self.sim_time = 0.0
        self.sim_timer = QTimer()
        self.sim_timer.timeout.connect(self.simulate_pose)
        self.sim_timer.start(100)  # update mỗi 100ms

    def simulate_pose(self):
        """Giả lập tọa độ thay đổi tuần hoàn"""
        self.sim_time += 0.1  # tăng thời gian
        x = 1.0 + 0.5 * math.cos(self.sim_time)  # dao động quanh x = 1.0
        y = 2.0 + 0.5 * math.sin(self.sim_time)  # dao động quanh y = 2.0
        theta = math.degrees(self.sim_time) % 360  # quay đều

        self.update_robot_position(x, y, theta)

    def update_robot_position(self, x, y, theta):
        px = (x - self.map_origin[0]) / self.map_resolution
        py = (self.map_height - (y - self.map_origin[1]) / self.map_resolution)

        def update():
            print(f"[SIM] px={px:.1f}, py={py:.1f}, θ={theta:.1f}")
            self.robot_item.setPos(px, py)
            self.robot_item.setRotation(-theta)

        QTimer.singleShot(0, update)


    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print("❌ Không thể load bản đồ:", path)
            return
        pixmap_item = self.map_scene.addPixmap(pixmap)
        self.map_scene.setSceneRect(QRectF(pixmap.rect()))  # Cập nhật kích thước scene
        self.ui.view_map.fitInView(pixmap_item, Qt.AspectRatioMode.KeepAspectRatio)
        self.map_height = pixmap.height()
