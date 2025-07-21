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
        self.browser.setUrl(QUrl("http://192.168.0.128:5000/"))  # web tu may anh 

        # Gan web 
        layout = self.ui.camera.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.camera)
            self.ui.camera.setLayout(layout)
        layout.addWidget(self.browser)
