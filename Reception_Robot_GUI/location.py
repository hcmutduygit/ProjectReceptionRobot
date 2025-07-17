
from PyQt6.QtWidgets import QWidget, QGraphicsScene
from PyQt6.QtGui import QPixmap, QBrush, QPen
from PyQt6.QtCore import Qt


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
