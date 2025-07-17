from PyQt6.QtWidgets import QWidget, QGraphicsScene, QGraphicsView, QGraphicsPolygonItem
from PyQt6.QtGui import QPixmap, QPolygonF, QWheelEvent, QPainter
from PyQt6.QtCore import QPointF


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

        # 5. Gan toa do 
        triangle = QPolygonF([
            QPointF(0, -10),   # Đầu mũi tên
            QPointF(5, 10),
            QPointF(-5, 10)
        ])

        robot_item = QGraphicsPolygonItem(triangle)
        self.map_scene.addItem(robot_item)

        x,y,theta = 150,120,90
        robot_item.setPos(x, y)
        robot_item.setTransformOriginPoint(0, 0)  # Tâm xoay tại điểm gốc hình tam giác
        robot_item.setRotation(theta)

    def load_map(self, path: str):
        pixmap = QPixmap(path)
        if pixmap.isNull():
            print("❌ Không thể load bản đồ:", path)
            return
        self.map_scene.addPixmap(pixmap)
'''
    def draw_robot_marker(self, x: float, y: float):
        self.map_scene.addEllipse(
            x, y, 10, 10,
            QPen(Qt.GlobalColor.red),
            QBrush(Qt.GlobalColor.red)
        )
'''
