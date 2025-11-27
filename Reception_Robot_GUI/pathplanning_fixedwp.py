# pathplanning.py
import numpy as np
from PyQt6.QtGui import QPen, QColor, QBrush
from PyQt6.QtCore import Qt, QPointF
import networkx as nx

class PathPlanner:
    def __init__(self, scene):
        self.scene = scene
        self.path_items = []
        self.locations = {}

        # === 4 fixed waypoints ===
        self.fixed_waypoints = { 
            "wp0": (649, 791),
            "wp1": (822, 785),
            "wp2": (808, 509),
            "wp3": (866, 504), 
            "wp4": (864, 381),
            "wp5": (850, 304),
            # "wp6": (835, 269),
            # "wp7": (736, 273),
            # "wp8": (735, 306),
        }

        # === graph ===
        self.graph_connections = {
            "wp0": ["wp1"],
            "wp1": ["wp0", "wp2"],
            "wp2": ["wp1", "wp3"],
            "wp3": ["wp2", "wp4"],
            "wp4": ["wp3", "wp5"],
            "wp5": ["wp4", "wp8", "wp6"],
            # "wp6": ["wp5", "wp7"],
            # "wp7": ["wp8", "wp6"],
            # "wp8": ["wp5", "wp7"],
        }

        self._draw_fixed_waypoints()

    def _draw_fixed_waypoints(self):
        for name, (x, y) in self.fixed_waypoints.items():
            r = 8
            brush = QBrush(QColor(0, 255, 0))
            pen = QPen(QColor(0, 0, 0), 1)
            self.scene.addEllipse(x - r, y - r, r * 2, r * 2, pen, brush)
            # text = self.scene.addText(name)
            # text.setDefaultTextColor(QColor(0, 0, 0))
            # text.setPos(x + 12, y - 15)

    def set_locations(self, locations: dict):
        self.locations = locations
        for name, (x, y) in locations.items():
            self._draw_marker(x, y, name)

    def _draw_marker(self, x, y, label):
        r = 8
        brush = QBrush(QColor(255, 200, 0))
        pen = QPen(QColor(0, 0, 0), 1)
        self.scene.addEllipse(x - r, y - r, r * 2, r * 2, pen, brush)
        text = self.scene.addText(label)
        text.setDefaultTextColor(QColor(0, 0, 0))
        text.setPos(x + 10, y - 12)

    # ======================================================
    # check if start/goal is on the segment between 2 wp 
    # ======================================================
    def _is_on_segment(self, point, wp1, wp2, tolerance=25):
        p = np.array(point)
        a = np.array(self.fixed_waypoints[wp1])
        b = np.array(self.fixed_waypoints[wp2])
        ab = b - a
        ap = p - a
        proj = np.dot(ap, ab) / np.dot(ab, ab)
        if proj < 0 or proj > 1:
            return False
        closest = a + proj * ab
        dist = np.linalg.norm(p - closest)
        return dist <= tolerance

    def _get_candidates(self, point):
        candidates = set()

        # is on segment or not 
        for wp1, neighbors in self.graph_connections.items():
            for wp2 in neighbors:
                if self._is_on_segment(point, wp1, wp2):
                    candidates.add(wp1)
                    candidates.add(wp2)

        # if not on segment -> choose the nearest wp 
        if not candidates:
            nearest = min(self.fixed_waypoints,
                          key=lambda wp: np.linalg.norm(np.array(point) - np.array(self.fixed_waypoints[wp])))
            candidates.add(nearest)

        return candidates

    # ==============================
    # DIJKSTRA + DOUBLE CONSTRAINT (start/goal is on segment of not)
    # ==============================
    def find_path(self, start_px, goal_label):
        if goal_label not in self.locations:
            raise ValueError(f"Goal '{goal_label}' not existed")

        goal_px = self.locations[goal_label]
        print(f"Finding path {start_px} → {goal_label}:{goal_px}...")

        # start constraint 
        start_candidates = self._get_candidates(start_px)

        # goal constraint 
        goal_candidates = self._get_candidates(goal_px)

        # graph 
        G = nx.Graph()

        for wp1, neighbors in self.graph_connections.items():
            for wp2 in neighbors:
                dist = np.linalg.norm(np.array(self.fixed_waypoints[wp1]) - np.array(self.fixed_waypoints[wp2]))
                G.add_edge(wp1, wp2, weight=dist)

        # find path 
        best_path = None
        min_cost = float('inf')

        for s_wp in start_candidates:
            for g_wp in goal_candidates:
                try:
                    path = nx.shortest_path(G, source=s_wp, target=g_wp, weight='weight')
                    cost = nx.shortest_path_length(G, source=s_wp, target=g_wp, weight='weight')
                    if cost < min_cost:
                        min_cost = cost
                        best_path = path
                        best_start_wp = s_wp
                        best_goal_wp = g_wp
                except nx.NetworkXNoPath:
                    continue

        if best_path is None:
            print("No valid path! Going direct.")
            path_coords = [start_px, goal_px]
        else:
            print(f"Optimal wp path: {best_path}")
            path_coords = [start_px]
            for wp in best_path:
                path_coords.append(self.fixed_waypoints[wp])
            path_coords.append(goal_px)

        self.draw_path(path_coords)
        return path_coords


    def draw_path(self, path):
        self.clear_path()
        if len(path) < 2:
            return
        pen = QPen(QColor(255, 0, 0), 1)
        pen.setStyle(Qt.PenStyle.DashLine)
        pen.setDashPattern([8, 4])
        for i in range(len(path) - 1):
            p1 = QPointF(path[i][0], path[i][1])
            p2 = QPointF(path[i + 1][0], path[i + 1][1])
            line = self.scene.addLine(p1.x(), p1.y(), p2.x(), p2.y(), pen)
            self.path_items.append(line)

    def clear_path(self):
        for item in self.path_items:
            self.scene.removeItem(item)
        self.path_items.clear()