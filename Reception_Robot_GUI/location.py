from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView
from PyQt6.QtGui import QPixmap, QBrush, QPen, QWheelEvent, QPainter
from PyQt6.QtCore import Qt


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

        # 1. Lấy layout hiện đang chứa view_map
        layout = self.ui.view_map.parent().layout()

        # 2. Xóa view_map cũ
        self.ui.view_map.setParent(None)

        # 3. Tạo MapGraphicsView thay thế
        self.ui.view_map = MapGraphicsView()
        layout.addWidget(self.ui.view_map)

        # 4. Gán scene và load ảnh
        self.ui.view_map.setScene(self.map_scene)
        self.load_map("resources/Map/map.png")
        self.draw_robot_marker(150, 120)

    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print("❌ Không thể load bản đồ:", path)
            return
        self.map_scene.addPixmap(pixmap)

    def draw_robot_marker(self, x: float, y: float):
        self.map_scene.addEllipse(
            x, y, 10, 10,
            QPen(Qt.GlobalColor.red),
            QBrush(Qt.GlobalColor.red)
        )
