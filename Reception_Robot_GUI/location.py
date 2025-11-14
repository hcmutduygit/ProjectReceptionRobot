from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer
import yaml, json, csv
import numpy as np
from datetime import datetime
import time 

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
        self.logging_active = False

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

    def get_goal_names(self):
        return list(self.goals.keys())  #for ui to automatically update label 

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
        # start_time = datetime.now()
        current_pos_map = self.last_position  # [x, y, theta] trong /map
        # goal_pixel = self.goals[goal]  # (px, py) trong pixel

        # Chuyển goal từ pixel → /map
        # x_map = self.map_origin[0] + goal_pixel[0] * self.map_resolution
        # y_map = self.map_origin[1] + (self.map_height - goal_pixel[1]) * self.map_resolution

        # Lập kế hoạch đường đi (pixel)
        self.planned_path = self.planner.find_path(self.robot_pos, goal)
        self.planner.draw_path(self.planned_path)

        # Chuyển toàn bộ planned_path từ pixel → /map
        self.plan_points = []
        for px, py in self.planned_path:
            x = self.map_origin[0] + px * self.map_resolution
            y = self.map_origin[1] + (self.map_height - py) * self.map_resolution
            self.plan_points.append({"x": round(x, 3), "y": round(y, 3)})

        # Bắt đầu từ vị trí hiện tại + danh sách kế hoạch
        current_wp = {"x": round(current_pos_map[0], 3), "y": round(current_pos_map[1], 3)}
        self.full_plan_points = [current_wp] + self.plan_points  # Lưu toàn bộ để xuất

        # Khởi tạo log
        self.log_data = []
        self.current_segment_idx = 0  # Chỉ số đoạn hiện tại: từ full_plan_points[i] → [i+1]
        self.threshold_to_next = 0.3  # meter
        self.last_log_time = 0

        # Bắt đầu timer log (100ms để check, nhưng chỉ ghi mỗi 1s)
        self.logging_active = True
        self.log_timer = QTimer(self)
        self.log_timer.timeout.connect(self.logging_step)
        self.log_timer.start(100)  # 10 Hz check

        # Gửi waypoints
        waypoints_json = json.dumps(self.full_plan_points, indent=2)
        print(f"Waypoints in /map coordinates (JSON): {waypoints_json}")
        publisher = WaypointsPublisher()
        publisher.publish_waypoints(waypoints_json)

    def logging_step(self):
        if not self.logging_active or len(self.full_plan_points) < 2:
            return

        now = time.time()
        if now - self.last_log_time < 1.0:
            return
        self.last_log_time = now

        actual_x = self.last_position[0]
        actual_y = self.last_position[1]
        timestamp = datetime.now()

        # Lấy đoạn hiện tại
        idx = self.current_segment_idx
        if idx + 1 >= len(self.full_plan_points):
            self.stop_logging()
            return

        p1 = self.full_plan_points[idx]
        p2 = self.full_plan_points[idx + 1]
        x1, y1 = p1["x"], p1["y"]
        x2, y2 = p2["x"], p2["y"]
        xr, yr = actual_x, actual_y

        # Vector
        vx, vy = x2 - x1, y2 - y1
        wx, wy = xr - x1, yr - y1
        c1 = wx * vx + wy * vy
        c2 = vx * vx + vy * vy

        if c2 == 0:
            t = 0.0
        else:
            t = max(0.0, min(1.0, c1 / c2))

        # Điểm chiếu lên đoạn thẳng
        plan_x = x1 + t * vx
        plan_y = y1 + t * vy

        # CTE
        error = np.hypot(xr - plan_x, yr - plan_y)

        # Ghi log
        self.log_data.append((timestamp, plan_x, plan_y, actual_x, actual_y, error))

        # Kiểm tra chuyển đoạn
        dist_to_next = np.hypot(xr - x2, yr - y2)
        if dist_to_next < self.threshold_to_next and idx + 2 < len(self.full_plan_points):
            self.current_segment_idx += 1

    def stop_logging(self):
        if hasattr(self, 'log_timer'):
            self.log_timer.stop()
        self.logging_active = False
        self.export_path_comparison()


    def export_path_comparison(self):
        if not hasattr(self, 'log_data') or len(self.log_data) == 0:
            print("Robot is not moving")
            return
        if not hasattr(self, 'full_plan_points') or len(self.full_plan_points) < 2:
            print("No planned path")
            return

        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_path = f"log_path/path_comparison_{timestamp_str}.csv"

        errors = [row[5] for row in self.log_data]

        with open(full_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'actual_x', 'actual_y', 'plan_x', 'plan_y', 'error_m'])
            for row in self.log_data:
                writer.writerow([
                    row[0].strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
                    round(row[3], 3),
                    round(row[4], 3),
                    round(row[1], 3),
                    round(row[2], 3),
                    round(row[5], 3)
                ])
            writer.writerow([])
            if errors:
                mean_error = np.mean(errors)
                max_error = np.max(errors)
                summary = f"Avg error: {mean_error:.3f}m | Max error: {max_error:.3f}m"
                writer.writerow([summary])

        print(f"Exported: {full_path}")

        # Reset
        self.log_data = []
        self.current_segment_idx = 0
        self.logging_active = False