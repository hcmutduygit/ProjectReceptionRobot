from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer
import yaml, json

from pathplanning_fixedwp import PathPlanner
from MQTT.waypoints_publisher import WaypointsPublisher 

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
    def __init__(self, view):
        super().__init__()
        self.ui = view
        self.map_scene = QGraphicsScene()

        layout = self.ui.parent().layout()
        self.ui.setParent(None)

        self.ui = MapGraphicsView()
        layout.addWidget(self.ui)
        self.ui.setScene(self.map_scene)

        self.load_map("Reception_Robot_GUI/resources/Map/map_fablab.pgm")

        # Tạo robot
        triangle = QPolygonF([
            QPointF(0, -15),
            QPointF(8, 20),
            QPointF(-8, 20)
        ])
        self.robot_item = QGraphicsPolygonItem(triangle)
        self.robot_item.setBrush(QBrush(QColor(101, 230, 248)))
        self.robot_item.setPen(QPen(Qt.GlobalColor.black, 1))
        self.robot_item.setTransformOriginPoint(0, 2)
        self.map_scene.addItem(self.robot_item)

        # Lưu trữ vị trí mới nhất
        self.last_position = [7.49, 17.07 , 0.0] #

        # Update GUI frequency 
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_robot_gui)
        self.update_timer.start(100)  # 100ms (10 Hz)

        # initial pathplanner 
        self.planner = PathPlanner(self.map_scene)
        self.planner.load_cost_map("Reception_Robot_GUI/resources/Map/map_fablab.pgm")

        # 4 goals 
        self.planner.set_locations({
            "A": (800, 1136),
            "B": (694, 583),
            "C": (1228, 431),
            "D": (733, 698)
        })

    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print(f"Cannot load map: {path}")
            return
        
        # Thêm ảnh vào scene và giữ lại object
        self.map_item = self.map_scene.addPixmap(pixmap)

        # Gán sceneRect đúng với kích thước ảnh (ảnh gốc là đơn vị pixel)
        self.map_scene.setSceneRect(0, 0, pixmap.width(), pixmap.height())
        
        # Fit hình ảnh vào view
        self.ui.fitInView(self.map_scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        # Lưu thông tin ảnh
        self.map_width = pixmap.width()
        self.map_height = pixmap.height()

        # Đọc thông số từ file map.yaml từ SLAM
        yaml_path = "Reception_Robot_GUI/resources/Map/map_fablab.yaml"
        try:
            with open(yaml_path, 'r') as file:
                map_config = yaml.safe_load(file)
                self.map_resolution = map_config['resolution']
                self.map_origin = (map_config['origin'][0], map_config['origin'][1])
        except Exception as e:
            print(f"Error while reading file map.yaml: {e}")


    def update_robot_gui(self):
        x, y, theta = self.last_position
        # Convert tọa độ từ /map sang GUI 
        py_raw = (y - self.map_origin[1]) / self.map_resolution 
        px_raw = (x - self.map_origin[0]) / self.map_resolution  
        px = px_raw
        py = self.map_height - py_raw
        # Thêm offset neu can  
        px += 0
        py += 0
        self.robot_pos = (px, py)
        self.robot_item.setPos(px, py)
        self.robot_item.setRotation(-theta+90)  

    def set_location(self, x, y, theta):
        """Update position from MQTT"""
        self.last_position = [x, y, theta]

    def plan_path(self, goal):
        path = self.planner.find_path(self.robot_pos, goal)
        self.planner.draw_path(path)

        waypoints = []
        for point in path:
            y_pixel, x_pixel = point  # (row, col)
            # Chuyển từ pixel sang tọa độ /map
            x_map = self.map_origin[0] + x_pixel * self.map_resolution
            y_map = self.map_origin[1] + (self.map_height - y_pixel) * self.map_resolution  # Đảo trục y
            waypoints.append({"x": round(x_map, 2), "y": round(y_map, 2)})
        waypoints_json = json.dumps(waypoints, indent=2)
        
        print(f"Waypoints in /map coordinates (JSON): {waypoints_json}")
        publisher = WaypointsPublisher()
        publisher.publish_waypoints(waypoints_json)
