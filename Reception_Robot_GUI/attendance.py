from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont


class AttendanceTab(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # truyền Ui_MainWindow từ file main

        # font va cac thuoc tinh khac 
        font = QFont("Roboto", 13)
        self.ui.table_attendance.setFont(font)
        
        self.ui.table_attendance.horizontalHeader().setFixedHeight(40)
        self.ui.table_attendance.verticalHeader().setDefaultSectionSize(40)

        header = self.ui.table_attendance.horizontalHeader()
        # do rong cot 
        for i in range(self.ui.table_attendance.columnCount() - 1):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)
            header.resizeSection(i, 200)
        header.setSectionResizeMode(self.ui.table_attendance.columnCount() - 1, QHeaderView.ResizeMode.Stretch)
        # so cot va ten 
        self.ui.table_attendance.setColumnCount(6)
        self.ui.table_attendance.setHorizontalHeaderLabels([
            "Employee ID", "Name", "Department", "Status","Check-in Time", "Email"
                ])
                
        self.ui.table_attendance.setStyleSheet("""
            QHeaderView::section {
                font-weight: bold;
                font-size: 13pt;}""")


        # Du lieu gia 
        self.attendance_data = [
            {"id": "E001", "name": "Ky", "dept": "HR", "email": "ky@example.com", "status": None, "time": None },
            {"id": "E002", "name": "Duy", "dept": "IT", "email": "phu@example.com", "status": None, "time": None },
            {"id": "E003", "name": "Phu", "dept": "Finance", "email": "duy@example.com", "status": None, "time": None },
            {"id": "E004", "name": "Thu", "dept": "Finance", "email": "thu@example.com", "status": None, "time": None },
            {"id": "E005", "name": "Loi", "dept": "Finance", "email": "loi@example.com", "status": None, "time": None },
            {"id": "E006", "name": "Thien", "dept": "Finance", "email": "thien@example.com", "status": None, "time": None },
        ]

        # Gan nut search 
        self.ui.search_btn.clicked.connect(self.search_attendance)

        # Hien thi bang 
        self.load_attendance_table(self.attendance_data)

    # hien bang 
    def load_attendance_table(self, data):
        self.ui.table_attendance.setRowCount(len(data))
        for row, entry in enumerate(data):
            self.ui.table_attendance.setItem(row, 0, QTableWidgetItem(entry["id"]))
            self.ui.table_attendance.setItem(row, 1, QTableWidgetItem(entry["name"]))
            self.ui.table_attendance.setItem(row, 2, QTableWidgetItem(entry["dept"]))
            self.ui.table_attendance.setItem(row, 3, QTableWidgetItem(entry.get("status") or "—"))
            self.ui.table_attendance.setItem(row, 4, QTableWidgetItem(entry.get("time") or "—"))
            self.ui.table_attendance.setItem(row, 5, QTableWidgetItem(entry["email"]))
        
    # ham cap nhat trang thai 
    def update_status(self, name=None, status=None, time=None):
        for entry in self.attendance_data:
            if (name and entry["name"] == name):
                entry["status"] = status
                entry["time"] = time
                break

        self.load_attendance_table(self.attendance_data)

    # ham search 
    def search_attendance(self):
        id_text = self.ui.lineEdit.text().strip().lower()
        name_text = self.ui.lineEdit_2.text().strip().lower()
        dept_text = self.ui.lineEdit_3.text().strip().lower()
        email_text = self.ui.lineEdit_4.text().strip().lower()

        filtered = []
        for entry in self.attendance_data:
            if (id_text in entry["id"].lower() and
                name_text in entry["name"].lower() and
                dept_text in entry["dept"].lower() and
                email_text in entry["email"].lower()):
                filtered.append(entry)

        self.load_attendance_table(filtered)
