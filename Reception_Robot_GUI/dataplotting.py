import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout

class PlotTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        # Khởi tạo biểu đồ
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')
        self.plot_widget.setTitle("📈 Real-Time Robot Data", color='black', size='14pt')

        # Hiển thị lưới
        self.plot_widget.showGrid(x=True, y=True)

        # Đặt nhãn trục
        self.plot_widget.setLabel('left', 'Value', units='unit')  # trục Y
        self.plot_widget.setLabel('bottom', 'Time', units='s')    # trục X

        # Cho phép zoom + pan
        self.plot_widget.setMouseEnabled(x=True, y=True)
        self.plot_widget.getViewBox().setLimits(xMin=0, yMin=0)

        # Đặt khoảng hiển thị mặc định
        self.plot_widget.setXRange(0, 10)
        self.plot_widget.setYRange(0, 40)

        # Nếu muốn: thêm chú thích
        self.plot_widget.addLegend()

        # Gắn layout
        layout = self.ui.data.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.data)
            self.ui.data.setLayout(layout)

        layout.addWidget(self.plot_widget)

        # Dữ liệu mẫu
        self.plot_widget.plot([0, 1, 2, 3], [10, 20, 10, 30], pen='b', name="Speed")
