from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import time
import numpy as np
from collections import deque

class PlotTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # --- Create the plot ---
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("📈 Real-Time Sin/Cos Scrolling", color='black', size='14pt')
        self.plot_widget.setLabel("left", "Value")
        self.plot_widget.setLabel("bottom", "Time (s)")
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.addLegend()
        self.plot_widget.setYRange(-1.5, 1.5)
        self.plot_widget.setXRange(0, 10)

        # Tạo layout mới (sử dụng data_container từ UI)
        layout = self.ui.data_container
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
        layout.addWidget(self.plot_widget)

        # Data and curve with initial data
        self.max_points = 1000
        self.x = deque(maxlen=self.max_points)
        self.y_sin = deque(maxlen=self.max_points)
        self.y_cos = deque(maxlen=self.max_points)
        self.start_time = time.time()

        # Add initial data
        for i in range(20):
            t = i * 0.5
            self.x.append(t)
            self.y_sin.append(np.sin(2 * np.pi * t))
            self.y_cos.append(np.cos(2 * np.pi * t))

        self.curve_sin = self.plot_widget.plot(pen=pg.mkPen('y', width=2), name='sin')
        self.curve_cos = self.plot_widget.plot(pen=pg.mkPen('c', width=2), name='cos')

        # Set initial data
        self.curve_sin.setData(list(self.x), list(self.y_sin))
        self.curve_cos.setData(list(self.x), list(self.y_cos))
        self.plot_widget.update()  # Ensure initial render

        # Timer update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)

    def update_plot(self):
        now = time.time() - self.start_time
        value_sin = np.sin(2 * np.pi * now)
        value_cos = np.cos(2 * np.pi * now)

        self.x.append(now)
        self.y_sin.append(value_sin)
        self.y_cos.append(value_cos)

        self.curve_sin.setData(list(self.x), list(self.y_sin))
        self.curve_cos.setData(list(self.x), list(self.y_cos))

        if now > 10:
            self.plot_widget.setXRange(now - 10, now)