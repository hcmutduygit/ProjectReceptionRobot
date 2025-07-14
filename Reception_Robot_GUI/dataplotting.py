import time
import math
import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout

class PlotTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # Khởi tạo biểu đồ
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("📈 Real-Time Robot Data", color='black', size='14pt')
        self.plot_widget.setLabel('left', 'Value', units='unit')
        self.plot_widget.setLabel('bottom', 'Time', units='s')
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setMouseEnabled(x=True, y=True)
        self.plot_widget.getViewBox().setLimits(xMin=0, yMin=0)
        self.plot_widget.setYRange(0, 40)
        self.plot_widget.setXRange(0, 10)
        self.plot_widget.enableAutoRange(False)  # chỉ auto Y
        self.plot_widget.addLegend()

        # Gắn vào layout trong ui
        layout = self.ui.data_container.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.ui.data_container.setLayout(layout)
        layout.addWidget(self.plot_widget)

        # Dữ liệu
        self.x = []
        self.y = []
        self.start_time = time.time()
        self.curve = self.plot_widget.plot(pen='b', name="Speed")

        # Timer cập nhật mỗi 100ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)

        print(">> Creating PlotTab")
        print(">> Layout exists:", self.ui.data_container.layout() is not None)


    def update_plot(self):
        # Giả lập dữ liệu: giá trị sin dao động
        t = time.time() - self.start_time
        value = math.sin(t) * 15 + 20

        self.x.append(t)
        self.y.append(value)

        # Giữ dữ liệu tối đa 60s (mỗi 0.1s → 600 điểm)
        if t > 60:
            self.x = self.x[-600:]
            self.y = self.y[-600:]

        if not self.x or not self.y or not math.isfinite(self.x[-1]) or not math.isfinite(self.y[-1]):
            return

        self.curve.setData(self.x, self.y)
        if self.x[-1] > 10:
            self.plot_widget.setXRange(self.x[-1] - 10, self.x[-1])
