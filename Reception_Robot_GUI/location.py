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
        self.ui = ui  # truyền Ui_MainWindow từ file main

        # Tạo scene và gán vào QGraphicsView
        scene = QGraphicsScene()
        pixmap = QPixmap("resources/Map/map.png")  # Ảnh bản đồ
        scene.addPixmap(pixmap)
        self.ui.view_map.setScene(scene)

        # Gợi ý lưu lại để sau này vẽ robot
        self.map_scene = scene
        x, y = 150, 120  # Tọa độ robot trên ảnh
        self.map_scene.addEllipse(x, y, 10, 10, QPen(Qt.GlobalColor.red), QBrush(Qt.GlobalColor.red))
