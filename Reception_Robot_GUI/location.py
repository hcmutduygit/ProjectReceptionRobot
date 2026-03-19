from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter, QBrush, QPen, QColor
from PyQt6.QtCore import QPointF, Qt, QTimer
import yaml, json
import numpy as np
from datetime import datetime

from pathplanning_fixedwp import PathPlanner
from logger import PathLogger
from MQTT.publisher_waypoints import WaypointsPublisher


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

        # Replace widget by graphics view
        layout = self.ui.parent().layout()
        self.ui.setParent(None)
        self.ui = MapGraphicsView()
        layout.addWidget(self.ui)

        self.map_scene = QGraphicsScene()
        self.ui.setScene(self.map_scene)

        # Logger
        self.logger = PathLogger()
        self.logger.location_tab = self

        # Load map
        self.load_map("Reception_Robot_GUI/resources/Map/new_map2.pgm")
        self.create_robot()

        # Goals
        self.goals = {
            "Restroom": (717, 505),
            "Water intake": (736, 269),
            "Chemistry hall": (835, 269),
            "Robotics lab": (464, 792),
            "Stairs": (820, 727),
            "Electrical lab": (1116, 778),
        }

        # Position
        self.last_position = [0.0, 0.0, 0.0]

        # Timer for robot GUI update
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_robot_gui)
        self.update_timer.start(100)

        # Path planner
        self.planner = PathPlanner(self.map_scene)
        self.planner.set_locations(self.goals)

        # Storage
        self.trajectory_items = []


    # ==========================================
    #                   MAP
    # ==========================================
    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print(f"Cannot load map: {path}")
            return
        
        self.map_item = self.map_scene.addPixmap(pixmap)
        self.map_scene.setSceneRect(0, 0, pixmap.width(), pixmap.height())
        self.ui.fitInView(self.map_scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        # Map info
        self.map_width = pixmap.width()
        self.map_height = pixmap.height()

        # YAML load
        yaml_path = "Reception_Robot_GUI/resources/Map/new_map2.yaml"
        try:
            with open(yaml_path, 'r') as file:
                map_config = yaml.safe_load(file)
                self.map_resolution = map_config['resolution']
                self.map_origin = (map_config['origin'][0], map_config['origin'][1])
        except Exception as e:
            print(f"Error reading YAML: {e}")


    # ==========================================
    #               ROBOT GRAPHICS
    # ==========================================
    def create_robot(self):
        pixmap = QPixmap("Reception_Robot_GUI/resources/Icons/robot.png")

        pixmap = pixmap.scaled(30, 30, 
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation)

        self.robot_item = QGraphicsPixmapItem(pixmap)
        self.robot_item.setZValue(100)

        self.robot_w = pixmap.width()
        self.robot_h = pixmap.height()

        self.map_scene.addItem(self.robot_item)

    # ==========================================
    #          ROBOT REAL POSITION UPDATE
    # ==========================================
    def update_robot_gui(self):
        x, y, theta = self.last_position

        # Convert map → pixel
        py = self.map_height - (y - self.map_origin[1]) / self.map_resolution
        px = (x - self.map_origin[0]) / self.map_resolution

        self.robot_pos = (px, py)
        self.robot_item.setPos(px - self.robot_w/2, py - self.robot_h/2)

        # Append trajectory if robot actually moves
        if hasattr(self, 'trajectory_points') and len(self.trajectory_points) > 0:
            current_point = (px, py)
            last_point = self.trajectory_points[-1]

            # Save point if far enough
            if np.linalg.norm(np.array(current_point) - np.array(last_point)) > 5:
                self.trajectory_points.append(current_point)
                self.trajectory_times.append(datetime.now())
                self.update_trajectory()


    def set_location(self, x, y, theta):
        self.last_position = [x, y, theta]


    # ==========================================
    #               TRAJECTORY
    # ==========================================
    def clear_trajectory(self):
        for item in self.trajectory_items:
            self.map_scene.removeItem(item)
        self.trajectory_items.clear()


    def update_trajectory(self):
        if len(self.trajectory_points) < 2:
            return

        # Clear old lines
        for item in self.trajectory_items:
            self.map_scene.removeItem(item)
        self.trajectory_items.clear()

        pen = QPen(QColor(180, 0, 0), 3)
        pen.setStyle(Qt.PenStyle.SolidLine)

        for i in range(len(self.trajectory_points) - 1):
            x1, y1 = self.trajectory_points[i]
            x2, y2 = self.trajectory_points[i + 1]
            line = self.map_scene.addLine(x1, y1, x2, y2, pen)
            self.trajectory_items.append(line)


    # ==========================================
    #                  PLANNING
    # ==========================================

    def get_goal_names(self):
        return list(self.goals.keys())  #for ui to automatically update label 

    def plan_path(self, goal):
        # Reset trajectory for new route
        self.clear_trajectory()
        self.trajectory_points = []
        self.trajectory_times = []

        # Add first point (robot's current pixel position)
        px, py = self.robot_pos
        self.trajectory_points.append((px, py))
        self.trajectory_times.append(datetime.now())

        # Plan path in pixels
        self.planned_path = self.planner.find_path(self.robot_pos, goal)
        self.planner.draw_path(self.planned_path)

        # Convert planned path pixel → map
        self.plan_points = []
        for px, py in self.planned_path:
            x = self.map_origin[0] + px * self.map_resolution
            y = self.map_origin[1] + (self.map_height - py) * self.map_resolution
            self.plan_points.append({"x": round(x, 3), "y": round(y, 3)})

        # Full waypoints including current
        curx, cury, _ = self.last_position
        current_wp = {"x": round(curx, 3), "y": round(cury, 3)}
        self.full_plan_points = [current_wp] + self.plan_points

        # Start logging
        self.logger.start_logging(self.full_plan_points)

        # Publish waypoints
        waypoints_json = json.dumps(self.full_plan_points, indent=2)
        print(f"Waypoints JSON:\n{waypoints_json}")
        publisher = WaypointsPublisher()
        publisher.publish_waypoints(waypoints_json)
