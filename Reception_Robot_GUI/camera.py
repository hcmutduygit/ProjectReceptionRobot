from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QLoggingCategory

# Tat log từ Qt WebEngine
QLoggingCategory.setFilterRules("qt.webenginecontext=false")

class CameraTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # Tạo widget web
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://youtu.be/3AtDnEC4zak?si=5fRzFzlAMZV1aSGj"))  # web tu may anh http://192.168.0.128:5000/

        # Gan web 
        layout = self.ui.camera_2.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.camera_2)
            self.ui.camera_2.setLayout(layout)
        layout.addWidget(self.browser)
