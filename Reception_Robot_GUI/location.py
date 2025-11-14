from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer
import yaml, json, csv
import numpy as np
from datetime import datetime 

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

        # 4 goals 
        self.goals = {
            "Robotics lab": (800, 1136),
            "Chemistry hall": (576, 513),
            "Electrical lab": (1228, 431),
            "Restroom": (704, 773)
        }

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
            # self.planner.load_cost_map("Reception_Robot_GUI/resources/Map/map_fablab.pgm")
        self.planner.set_locations(self.goals)
        self.trajectory_items = []

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
        py = self.map_height - (y - self.map_origin[1]) / self.map_resolution 
        px = (x - self.map_origin[0]) / self.map_resolution  

        self.robot_pos = (px, py)
        self.robot_item.setPos(px, py)
        self.robot_item.setRotation(theta -270 + 30)  

        if hasattr(self, 'trajectory_points') and len(self.trajectory_points) > 0:
            current_point = (px, py)
            current_time = datetime.now()
            
            last_point = self.trajectory_points[-1]
            if np.linalg.norm(np.array(current_point) - np.array(last_point)) > 5: #save if point is >5 pixel compare to last point 
                self.trajectory_points.append(current_point)
                self.trajectory_times.append(current_time)
                self.update_trajectory()

    def set_location(self, x, y, theta):
        """Update position from MQTT"""
        self.last_position = [x, y, theta]

    def update_trajectory(self):
        """Vẽ quỹ đạo realtime của robot (nét liền đỏ rượu)"""
        if len(self.trajectory_points) < 2:
            return

        # Clear the old one 
        for item in self.trajectory_items:
            self.map_scene.removeItem(item)
        self.trajectory_items.clear()

        pen = QPen(QColor(180, 0, 0), 3)
        pen.setStyle(Qt.PenStyle.SolidLine)

        for i in range(len(self.trajectory_points) - 1):
            p1 = QPointF(self.trajectory_points[i][0], self.trajectory_points[i][1])
            p2 = QPointF(self.trajectory_points[i+1][0], self.trajectory_points[i+1][1])
            line = self.map_scene.addLine(p1.x(), p1.y(), p2.x(), p2.y(), pen)
            self.trajectory_items.append(line)

    def plan_path(self, goal):
        start_time = datetime.now()
        self.trajectory_points = [self.robot_pos]
        self.trajectory_times  = [start_time]
        self.update_trajectory() # Start drawing with robot position and time after had choosing any goal 
        
        self.planned_path = self.planner.find_path(self.robot_pos, goal)
        self.planner.draw_path(self.planned_path)

        waypoints = []
        for point in self.planned_path:
            x_pixel, y_pixel = point  # (x,y)
            # pixel to /map
            x_map = self.map_origin[0] + x_pixel * self.map_resolution
            y_map = self.map_origin[1] + (self.map_height - y_pixel) * self.map_resolution  # Đảo trục y
            waypoints.append({"x": round(x_map, 2), "y": round(y_map, 2)})
        waypoints_json = json.dumps(waypoints, indent=2)
        
        print(f"Waypoints in /map coordinates (JSON): {waypoints_json}")
        publisher = WaypointsPublisher()
        publisher.publish_waypoints(waypoints_json)

    def get_goal_names(self):
        return list(self.goals.keys())  #for ui to automatically update label 

    def export_path_comparison(self):
        if not hasattr(self, 'planned_path') or len(self.planned_path) == 0:
            print("No planned path.")
            return
        if len(self.trajectory_points) < 2:
            print("Robot chưa di chuyển.")
            return

        # === TẠO THƯ MỤC ===
        import os
        comp_dir = os.path.join(os.path.dirname(__file__), 'comparison')
        os.makedirs(comp_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_path = os.path.join(comp_dir, f"path_comparison_{timestamp}.csv")

        # === CHUYỂN PIXEL → /MAP ===
        def pixel_to_map(p):
            x, y = p
            return round(self.map_origin[0] + x * self.map_resolution, 3), \
                round(self.map_origin[1] + (self.map_height - y) * self.map_resolution, 3)

        planned_map = [pixel_to_map(p) for p in self.planned_path]
        actual_map  = [pixel_to_map(p) for p in self.trajectory_points]
        actual_times = [t.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] for t in self.trajectory_times]

        # === NỘI SUY ===
        from scipy.interpolate import interp1d
        planned_np = np.array(planned_map)
        actual_np  = np.array(actual_map)

        dist_planned = np.cumsum(np.linalg.norm(np.diff(planned_np, axis=0), axis=1))
        dist_planned = np.insert(dist_planned, 0, 0)
        dist_actual  = np.cumsum(np.linalg.norm(np.diff(actual_np, axis=0), axis=1))
        dist_actual  = np.insert(dist_actual, 0, 0)

        interp_x = interp1d(dist_planned, planned_np[:, 0], kind='linear', fill_value="extrapolate")
        interp_y = interp1d(dist_planned, planned_np[:, 1], kind='linear', fill_value="extrapolate")
        interp_x_vals = interp_x(dist_actual)
        interp_y_vals = interp_y(dist_actual)
        errors = np.linalg.norm(np.stack((interp_x_vals - actual_np[:, 0],
                                        interp_y_vals - actual_np[:, 1]), axis=1), axis=1)

        # === GHI CSV ===
        with open(full_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'actual_x', 'actual_y', 'plan_x', 'plan_y', 'error_m'])
            for i in range(len(actual_map)):
                writer.writerow([actual_times[i], actual_map[i][0], actual_map[i][1],
                                round(interp_x_vals[i], 3), round(interp_y_vals[i], 3), round(errors[i], 3)])
            writer.writerow([])
            summary = f"Avg error: {np.mean(errors):.3f}m | Max error: {np.max(errors):.3f}m"
            writer.writerow([summary])

        print(f"Exported: {full_path}")