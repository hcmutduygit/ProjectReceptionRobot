from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

class CameraTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # Tạo widget web
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://192.168.0.128:5000/"))  # Đổi thành web thật

        # Gắn browser vào layout của camera container
        layout = self.ui.camera.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.camera)
            self.ui.camera.setLayout(layout)
        layout.addWidget(self.browser)
