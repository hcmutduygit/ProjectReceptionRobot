from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import time
from collections import deque


class PlotTelemetry(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # --- 3 layout đã có sẵn trong Qt Designer ---
        self.layout_imu  = self.ui.imupac
        self.layout_odom = self.ui.odompac
        self.layout_cte  = self.ui.cte

        # --- Check xem còn widget cũ k --- 
        for lay in (self.layout_imu, self.layout_odom, self.layout_cte):
            while lay.count():
                item = lay.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()

        # --- Tạo 3 PlotWidget ---
        self.plot_imu = pg.PlotWidget(title="IMU Packet Loss (%)")
        self.plot_odom = pg.PlotWidget(title="Odom Packet Loss (%)")
        self.plot_cte = pg.PlotWidget(title="CTE Error (m)")

        # --- Style chung --- 
        for p in (self.plot_imu, self.plot_odom, self.plot_cte):
            p.setBackground('w')
            p.showGrid(x=True, y=True)
            p.setLabel('left', color='black', size='10pt')
            p.setLabel('bottom', 'Time (s)', color='black', size='10pt')

        # --- Thêm vào đúng layout tương ứng --- 
        self.layout_imu.addWidget(self.plot_imu)
        self.layout_odom.addWidget(self.plot_odom)
        self.layout_cte.addWidget(self.plot_cte)

        # --- Data buffers ---
        self.max_points = 1000
        self.t_imu = deque(maxlen=self.max_points)
        self.v_imu = deque(maxlen=self.max_points)

        self.t_odom = deque(maxlen=self.max_points)
        self.v_odom = deque(maxlen=self.max_points)

        self.t_cte = deque(maxlen=self.max_points)
        self.v_cte = deque(maxlen=self.max_points)

        self.start_time = time.time()

        # --- Curves ---
        self.curve_imu  = self.plot_imu.plot( pen=pg.mkPen('#e74c3c', width=2), name="IMU Loss")
        self.curve_odom = self.plot_odom.plot(pen=pg.mkPen('#3498db', width=2), name="Odom Loss")
        self.curve_cte  = self.plot_cte.plot( pen=pg.mkPen('#2ecc71', width=2), name="CTE")

        # --- Timers ---
        self.timer_imu = QTimer(self)
        self.timer_imu.timeout.connect(self.update_imu)
        self.timer_imu.start(10000)     # IMU packet loss 10s 

        self.timer_odom = QTimer(self)
        self.timer_odom.timeout.connect(self.update_odom)
        self.timer_odom.start(10000)    # Odom packet loss 10s 

        self.timer_cte = QTimer(self)
        self.timer_cte.timeout.connect(self.update_cte)
        self.timer_cte.start(1000)      # CTE 1s

    # ==============================================================

    def update_imu(self):
        now = time.time() - self.start_time
        value = self._get_imu_packet_loss()
        self.t_imu.append(now)
        self.v_imu.append(value)
        self.curve_imu.setData(self.t_imu, self.v_imu)
        self.plot_imu.setXRange(max(0, now - 120), now)   # show the last 2 minutes 

    def update_odom(self):
        now = time.time() - self.start_time
        value = self._get_odom_packet_loss()
        self.t_odom.append(now)
        self.v_odom.append(value)
        self.curve_odom.setData(self.t_odom, self.v_odom)
        self.plot_odom.setXRange(max(0, now - 120), now)   # show the last 2 minutes 

    def update_cte(self):
        now = time.time() - self.start_time
        value = self._get_cte_error()
        self.t_cte.append(now)
        self.v_cte.append(value)
        self.curve_cte.setData(self.t_cte, self.v_cte)
        self.plot_cte.setXRange(max(0, now - 15), now)   # show the last 15 secs

    # ==============================================================

    def _get_imu_packet_loss(self):
        import random
        return random.uniform(0, 8)

    def _get_odom_packet_loss(self):
        import random
        return random.uniform(0, 10)

    def _get_cte_error(self):
        import random
        return random.uniform(-0.6, 0.6)