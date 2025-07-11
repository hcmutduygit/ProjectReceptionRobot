# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Robot_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from resources import resources_rc
from resources import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1440, 900)
        MainWindow.setMinimumSize(QSize(1440, 900))
        MainWindow.setMaximumSize(QSize(2340, 1080))
        font = QFont()
        font.setFamilies([u"Roboto"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/logo/icon_APP.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"font-family:  \"Roboto\";\n"
"}")
        MainWindow.setIconSize(QSize(0, 0))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1440, 900))
        self.centralwidget.setMaximumSize(QSize(2340, 1080))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Dashboard = QStackedWidget(self.centralwidget)
        self.Dashboard.setObjectName(u"Dashboard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dashboard.sizePolicy().hasHeightForWidth())
        self.Dashboard.setSizePolicy(sizePolicy)
        self.Dashboard.setMinimumSize(QSize(260, 900))
        self.Dashboard.setMaximumSize(QSize(350, 1080))
        self.Dashboard.setFont(font)
        self.Dashboard.setStyleSheet(u"*{\n"
"	background-color: rgb(0, 41, 77);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(197, 225, 248);\n"
"	color: rgb(159, 190, 252);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:  0px;\n"
"text-align: left;\n"
"padding-left: 30px;\n"
"spacing: 10px;\n"
"}\n"
"")
        self.Dashboard.setFrameShape(QFrame.NoFrame)
        self.Dashboard.setFrameShadow(QFrame.Plain)
        self.Dashboard.setLineWidth(0)
        self.Dashboard_signin = QWidget()
        self.Dashboard_signin.setObjectName(u"Dashboard_signin")
        self.Dashboard_signin.setMinimumSize(QSize(260, 800))
        self.Dashboard_signin.setMaximumSize(QSize(350, 1080))
        self.Dashboard_signin.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207))\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Dashboard_signin)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Signin_logo = QFrame(self.Dashboard_signin)
        self.Signin_logo.setObjectName(u"Signin_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Signin_logo.sizePolicy().hasHeightForWidth())
        self.Signin_logo.setSizePolicy(sizePolicy1)
        self.Signin_logo.setMinimumSize(QSize(260, 150))
        self.Signin_logo.setMaximumSize(QSize(16777215, 300))
        self.Signin_logo.setStyleSheet(u"")
        self.Signin_logo.setFrameShape(QFrame.NoFrame)
        self.Signin_logo.setFrameShadow(QFrame.Plain)
        self.Signin_logo.setLineWidth(0)
        self.gridLayout_4 = QGridLayout(self.Signin_logo)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(12)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(20, 25, 20, 20)
        self.Logo_BK = QLabel(self.Signin_logo)
        self.Logo_BK.setObjectName(u"Logo_BK")
        sizePolicy.setHeightForWidth(self.Logo_BK.sizePolicy().hasHeightForWidth())
        self.Logo_BK.setSizePolicy(sizePolicy)
        self.Logo_BK.setMinimumSize(QSize(50, 50))
        self.Logo_BK.setMaximumSize(QSize(150, 150))
        self.Logo_BK.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_BK.setFrameShape(QFrame.NoFrame)
        self.Logo_BK.setPixmap(QPixmap(u":/logos/Logos/Logo BK.png"))
        self.Logo_BK.setScaledContents(True)
        self.Logo_BK.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Logo_BK, 0, 1, 1, 1)

        self.Logo_fab = QLabel(self.Signin_logo)
        self.Logo_fab.setObjectName(u"Logo_fab")
        sizePolicy.setHeightForWidth(self.Logo_fab.sizePolicy().hasHeightForWidth())
        self.Logo_fab.setSizePolicy(sizePolicy)
        self.Logo_fab.setMinimumSize(QSize(50, 50))
        self.Logo_fab.setMaximumSize(QSize(150, 150))
        self.Logo_fab.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_fab.setPixmap(QPixmap(u":/logos/Logos/Fablab Logo-aftercut.png"))
        self.Logo_fab.setScaledContents(True)
        self.Logo_fab.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Logo_fab, 0, 2, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)

        self.verticalLayout_3.addWidget(self.Signin_logo)

        self.Signin_line = QFrame(self.Dashboard_signin)
        self.Signin_line.setObjectName(u"Signin_line")
        self.Signin_line.setEnabled(True)
        self.Signin_line.setMinimumSize(QSize(260, 20))
        self.Signin_line.setMaximumSize(QSize(350, 20))
        self.Signin_line.setFrameShape(QFrame.NoFrame)
        self.Signin_line.setFrameShadow(QFrame.Raised)
        self.Signin_line.setLineWidth(0)
        self.gridLayout = QGridLayout(self.Signin_line)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Line = QFrame(self.Signin_line)
        self.Line.setObjectName(u"Line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Line.sizePolicy().hasHeightForWidth())
        self.Line.setSizePolicy(sizePolicy2)
        self.Line.setMinimumSize(QSize(210, 3))
        self.Line.setMaximumSize(QSize(250, 3))
        self.Line.setSizeIncrement(QSize(0, 0))
        self.Line.setLayoutDirection(Qt.LeftToRight)
        self.Line.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.Line.setFrameShape(QFrame.NoFrame)
        self.Line.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.Line, 0, 0, 1, 1, Qt.AlignHCenter)

        self.Line_2 = QFrame(self.Signin_line)
        self.Line_2.setObjectName(u"Line_2")
        self.Line_2.setMinimumSize(QSize(160, 3))
        self.Line_2.setMaximumSize(QSize(200, 3))
        self.Line_2.setLayoutDirection(Qt.LeftToRight)
        self.Line_2.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.Line_2.setFrameShape(QFrame.NoFrame)
        self.Line_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.Line_2, 1, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.Signin_line)

        self.Signin_btn = QFrame(self.Dashboard_signin)
        self.Signin_btn.setObjectName(u"Signin_btn")
        self.Signin_btn.setMinimumSize(QSize(260, 660))
        self.Signin_btn.setMaximumSize(QSize(350, 700))
        self.Signin_btn.setStyleSheet(u"")
        self.Signin_btn.setFrameShape(QFrame.NoFrame)
        self.Signin_btn.setFrameShadow(QFrame.Raised)
        self.Signin_btn.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.Signin_btn)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 150, 0, 150)
        self.Signin_btn_signin = QPushButton(self.Signin_btn)
        self.Signin_btn_signin.setObjectName(u"Signin_btn_signin")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Signin_btn_signin.sizePolicy().hasHeightForWidth())
        self.Signin_btn_signin.setSizePolicy(sizePolicy3)
        self.Signin_btn_signin.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(24)
        font1.setBold(False)
        self.Signin_btn_signin.setFont(font1)
        self.Signin_btn_signin.setFocusPolicy(Qt.NoFocus)
        self.Signin_btn_signin.setStyleSheet(u"")
        self.Signin_btn_signin.setIconSize(QSize(35, 35))
        self.Signin_btn_signin.setAutoRepeat(True)
        self.Signin_btn_signin.setAutoExclusive(False)
        self.Signin_btn_signin.setAutoRepeatDelay(0)
        self.Signin_btn_signin.setAutoRepeatInterval(0)

        self.verticalLayout_2.addWidget(self.Signin_btn_signin)

        self.Signin_btn_signup = QPushButton(self.Signin_btn)
        self.Signin_btn_signup.setObjectName(u"Signin_btn_signup")
        sizePolicy3.setHeightForWidth(self.Signin_btn_signup.sizePolicy().hasHeightForWidth())
        self.Signin_btn_signup.setSizePolicy(sizePolicy3)
        self.Signin_btn_signup.setMaximumSize(QSize(16777215, 50))
        self.Signin_btn_signup.setFont(font1)
        self.Signin_btn_signup.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_2.addWidget(self.Signin_btn_signup)

        self.verticalLayout_2.setStretch(1, 1)
        self.Signin_btn_signup.raise_()
        self.Signin_btn_signin.raise_()

        self.verticalLayout_3.addWidget(self.Signin_btn)

        self.Signin_text = QLabel(self.Dashboard_signin)
        self.Signin_text.setObjectName(u"Signin_text")
        self.Signin_text.setMinimumSize(QSize(260, 70))
        self.Signin_text.setMaximumSize(QSize(350, 70))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(True)
        self.Signin_text.setFont(font2)
        self.Signin_text.setLayoutDirection(Qt.LeftToRight)
        self.Signin_text.setStyleSheet(u"")
        self.Signin_text.setScaledContents(False)
        self.Signin_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Signin_text, 0, Qt.AlignBottom)

        self.verticalLayout_3.setStretch(0, 170)
        self.verticalLayout_3.setStretch(2, 820)
        self.verticalLayout_3.setStretch(3, 70)
        self.Dashboard.addWidget(self.Dashboard_signin)
        self.Dashboard_main = QWidget()
        self.Dashboard_main.setObjectName(u"Dashboard_main")
        sizePolicy.setHeightForWidth(self.Dashboard_main.sizePolicy().hasHeightForWidth())
        self.Dashboard_main.setSizePolicy(sizePolicy)
        self.Dashboard_main.setMinimumSize(QSize(240, 900))
        self.Dashboard_main.setMaximumSize(QSize(350, 1080))
        self.Dashboard_main.setFont(font)
        self.Dashboard_main.setStyleSheet(u"QWidget {\n"
"background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207))\n"
"}")
        self.verticalLayout = QVBoxLayout(self.Dashboard_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_Logo = QFrame(self.Dashboard_main)
        self.Main_Logo.setObjectName(u"Main_Logo")
        sizePolicy.setHeightForWidth(self.Main_Logo.sizePolicy().hasHeightForWidth())
        self.Main_Logo.setSizePolicy(sizePolicy)
        self.Main_Logo.setMinimumSize(QSize(260, 100))
        self.Main_Logo.setMaximumSize(QSize(16777215, 300))
        self.Main_Logo.setStyleSheet(u"")
        self.Main_Logo.setFrameShape(QFrame.NoFrame)
        self.Main_Logo.setFrameShadow(QFrame.Plain)
        self.Main_Logo.setLineWidth(0)
        self.gridLayout_5 = QGridLayout(self.Main_Logo)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setHorizontalSpacing(12)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(20, 25, 20, 20)
        self.Logo_BK_2 = QLabel(self.Main_Logo)
        self.Logo_BK_2.setObjectName(u"Logo_BK_2")
        sizePolicy.setHeightForWidth(self.Logo_BK_2.sizePolicy().hasHeightForWidth())
        self.Logo_BK_2.setSizePolicy(sizePolicy)
        self.Logo_BK_2.setMinimumSize(QSize(100, 100))
        self.Logo_BK_2.setMaximumSize(QSize(150, 150))
        self.Logo_BK_2.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_BK_2.setPixmap(QPixmap(u":/logos/Logos/Logo BK.png"))
        self.Logo_BK_2.setScaledContents(True)
        self.Logo_BK_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Logo_BK_2, 0, 1, 1, 1)

        self.Logo_fab_2 = QLabel(self.Main_Logo)
        self.Logo_fab_2.setObjectName(u"Logo_fab_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Logo_fab_2.sizePolicy().hasHeightForWidth())
        self.Logo_fab_2.setSizePolicy(sizePolicy4)
        self.Logo_fab_2.setMinimumSize(QSize(100, 100))
        self.Logo_fab_2.setMaximumSize(QSize(150, 150))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setBold(True)
        self.Logo_fab_2.setFont(font3)
        self.Logo_fab_2.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"border-radius:  15px;")
        self.Logo_fab_2.setPixmap(QPixmap(u":/logos/Logos/Fablab Logo-aftercut.png"))
        self.Logo_fab_2.setScaledContents(True)
        self.Logo_fab_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Logo_fab_2, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.Main_Logo)

        self.Main_btn = QFrame(self.Dashboard_main)
        self.Main_btn.setObjectName(u"Main_btn")
        sizePolicy.setHeightForWidth(self.Main_btn.sizePolicy().hasHeightForWidth())
        self.Main_btn.setSizePolicy(sizePolicy)
        self.Main_btn.setMinimumSize(QSize(260, 750))
        self.Main_btn.setMaximumSize(QSize(16777215, 780))
        self.Main_btn.setFont(font)
        self.Main_btn.setStyleSheet(u"")
        self.Main_btn.setFrameShape(QFrame.NoFrame)
        self.Main_btn.setFrameShadow(QFrame.Raised)
        self.Main_btn.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.Main_btn)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Main_line = QFrame(self.Main_btn)
        self.Main_line.setObjectName(u"Main_line")
        self.Main_line.setMinimumSize(QSize(260, 20))
        self.Main_line.setMaximumSize(QSize(16777215, 20))
        self.Main_line.setContextMenuPolicy(Qt.NoContextMenu)
        self.Main_line.setFrameShape(QFrame.NoFrame)
        self.Main_line.setFrameShadow(QFrame.Raised)
        self.Main_line.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.Main_line)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.Line_3 = QFrame(self.Main_line)
        self.Line_3.setObjectName(u"Line_3")
        sizePolicy.setHeightForWidth(self.Line_3.sizePolicy().hasHeightForWidth())
        self.Line_3.setSizePolicy(sizePolicy)
        self.Line_3.setMaximumSize(QSize(16777215, 3))
        self.Line_3.setSizeIncrement(QSize(0, 0))
        self.Line_3.setLayoutDirection(Qt.LeftToRight)
        self.Line_3.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.Line_3.setFrameShape(QFrame.NoFrame)
        self.Line_3.setFrameShadow(QFrame.Raised)
        self.Line_3.setLineWidth(3)

        self.horizontalLayout_2.addWidget(self.Line_3)


        self.verticalLayout_6.addWidget(self.Main_line)

        self.Main__frame_admin = QFrame(self.Main_btn)
        self.Main__frame_admin.setObjectName(u"Main__frame_admin")
        self.Main__frame_admin.setMaximumSize(QSize(16777215, 600))
        self.Main__frame_admin.setFrameShape(QFrame.NoFrame)
        self.Main__frame_admin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Main__frame_admin)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Label_admin = QLabel(self.Main__frame_admin)
        self.Label_admin.setObjectName(u"Label_admin")
        self.Label_admin.setMinimumSize(QSize(0, 20))
        self.Label_admin.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(19)
        self.Label_admin.setFont(font4)
        self.Label_admin.setStyleSheet(u"color: rgb(101, 230, 248);\n"
"margin-left: 10px;\n"
"")
        self.Label_admin.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Label_admin.setMargin(0)

        self.verticalLayout_8.addWidget(self.Label_admin)

        self.Main_btn_attendance = QPushButton(self.Main__frame_admin)
        self.Main_btn_attendance.setObjectName(u"Main_btn_attendance")
        self.Main_btn_attendance.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(18)
        font5.setKerning(True)
        self.Main_btn_attendance.setFont(font5)
        self.Main_btn_attendance.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_attendance.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_attendance)

        self.Main_btn_camera = QPushButton(self.Main__frame_admin)
        self.Main_btn_camera.setObjectName(u"Main_btn_camera")
        self.Main_btn_camera.setMinimumSize(QSize(0, 40))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(18)
        self.Main_btn_camera.setFont(font6)
        self.Main_btn_camera.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_camera.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_camera)

        self.Main_btn_tracking = QPushButton(self.Main__frame_admin)
        self.Main_btn_tracking.setObjectName(u"Main_btn_tracking")
        self.Main_btn_tracking.setMinimumSize(QSize(0, 40))
        self.Main_btn_tracking.setFont(font6)
        self.Main_btn_tracking.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_tracking.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_tracking)

        self.Main_btn_robotstatus = QPushButton(self.Main__frame_admin)
        self.Main_btn_robotstatus.setObjectName(u"Main_btn_robotstatus")
        self.Main_btn_robotstatus.setMinimumSize(QSize(0, 40))
        self.Main_btn_robotstatus.setFont(font6)
        self.Main_btn_robotstatus.setFocusPolicy(Qt.NoFocus)
        self.Main_btn_robotstatus.setFlat(True)

        self.verticalLayout_8.addWidget(self.Main_btn_robotstatus)

        self.Main_btn_data = QPushButton(self.Main__frame_admin)
        self.Main_btn_data.setObjectName(u"Main_btn_data")
        self.Main_btn_data.setMinimumSize(QSize(0, 40))
        self.Main_btn_data.setFont(font6)

        self.verticalLayout_8.addWidget(self.Main_btn_data)


        self.verticalLayout_6.addWidget(self.Main__frame_admin)

        self.Main_frame_admin = QFrame(self.Main_btn)
        self.Main_frame_admin.setObjectName(u"Main_frame_admin")
        self.Main_frame_admin.setMaximumSize(QSize(16777215, 200))
        self.Main_frame_admin.setFrameShape(QFrame.NoFrame)
        self.Main_frame_admin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Main_frame_admin)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Account_username = QLabel(self.Main_frame_admin)
        self.Account_username.setObjectName(u"Account_username")
        self.Account_username.setMinimumSize(QSize(0, 20))
        self.Account_username.setMaximumSize(QSize(16777215, 30))
        self.Account_username.setFont(font6)
        self.Account_username.setStyleSheet(u"color: rgb(101, 230, 248);\n"
"margin-left: 10px;\n"
"")
        self.Account_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Account_username.setMargin(0)

        self.verticalLayout_9.addWidget(self.Account_username)

        self.Account__btnlogout = QPushButton(self.Main_frame_admin)
        self.Account__btnlogout.setObjectName(u"Account__btnlogout")
        self.Account__btnlogout.setMinimumSize(QSize(0, 40))
        self.Account__btnlogout.setFont(font6)
        self.Account__btnlogout.setFocusPolicy(Qt.NoFocus)
        self.Account__btnlogout.setFlat(True)

        self.verticalLayout_9.addWidget(self.Account__btnlogout)


        self.verticalLayout_6.addWidget(self.Main_frame_admin)


        self.verticalLayout.addWidget(self.Main_btn)

        self.verticalLayout.setStretch(1, 1)
        self.Dashboard.addWidget(self.Dashboard_main)

        self.horizontalLayout.addWidget(self.Dashboard)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.verticalLayout_16 = QVBoxLayout(self.widget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 30))
        self.frame_3.setStyleSheet(u"\n"
"color: rgb(0, 41, 77);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"border-radius: 20px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(30, 30))
        self.label_8.setMaximumSize(QSize(50, 50))
        self.label_8.setPixmap(QPixmap(u":/Icons/Icons/mqtt_icon.svg"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.label_mqtt = QLabel(self.frame_2)
        self.label_mqtt.setObjectName(u"label_mqtt")
        sizePolicy.setHeightForWidth(self.label_mqtt.sizePolicy().hasHeightForWidth())
        self.label_mqtt.setSizePolicy(sizePolicy)
        self.label_mqtt.setMinimumSize(QSize(0, 30))
        self.label_mqtt.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_mqtt.setFont(font7)
        self.label_mqtt.setTextFormat(Qt.PlainText)

        self.horizontalLayout_10.addWidget(self.label_mqtt)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"border-radius: 20px;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_battery = QLabel(self.frame)
        self.label_battery.setObjectName(u"label_battery")
        sizePolicy.setHeightForWidth(self.label_battery.sizePolicy().hasHeightForWidth())
        self.label_battery.setSizePolicy(sizePolicy)
        self.label_battery.setMinimumSize(QSize(0, 30))
        self.label_battery.setMaximumSize(QSize(16777215, 50))
        self.label_battery.setFont(font7)
        self.label_battery.setStyleSheet(u"")
        self.label_battery.setFrameShape(QFrame.StyledPanel)
        self.label_battery.setFrameShadow(QFrame.Raised)
        self.label_battery.setScaledContents(False)
        self.label_battery.setAlignment(Qt.AlignCenter)
        self.label_battery.setMargin(5)
        self.label_battery.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_battery)


        self.horizontalLayout_7.addWidget(self.frame)


        self.verticalLayout_16.addWidget(self.frame_3)

        self.Page = QStackedWidget(self.widget)
        self.Page.setObjectName(u"Page")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Page.sizePolicy().hasHeightForWidth())
        self.Page.setSizePolicy(sizePolicy6)
        self.Page.setMinimumSize(QSize(1180, 850))
        self.Page.setMaximumSize(QSize(1995, 1050))
        self.Page.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.Page.setFrameShadow(QFrame.Raised)
        self.Page.setLineWidth(0)
        self.Page_signin = QWidget()
        self.Page_signin.setObjectName(u"Page_signin")
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(9)
        font8.setBold(False)
        self.Page_signin.setFont(font8)
        self.Page_signin.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.gridLayout_2 = QGridLayout(self.Page_signin)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Sigin_form = QFrame(self.Page_signin)
        self.Sigin_form.setObjectName(u"Sigin_form")
        self.Sigin_form.setMaximumSize(QSize(720, 360))
        self.Sigin_form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.Sigin_form.setFrameShape(QFrame.NoFrame)
        self.Sigin_form.setFrameShadow(QFrame.Raised)
        self.Sigin_form.setLineWidth(5)
        self.formLayout_2 = QFormLayout(self.Sigin_form)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignCenter)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 25)
        self.Title = QFrame(self.Sigin_form)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(720, 80))
        self.Title.setMaximumSize(QSize(720, 80))
        self.Title.setStyleSheet(u"color: rgb(0, 41, 77);")
        self.Title.setFrameShape(QFrame.NoFrame)
        self.Title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Title)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Title)
        self.label_2.setObjectName(u"label_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy7)
        self.label_2.setMinimumSize(QSize(720, 0))
        self.label_2.setMaximumSize(QSize(720, 100))
        font9 = QFont()
        font9.setFamilies([u"Roboto"])
        font9.setPointSize(26)
        font9.setBold(True)
        self.label_2.setFont(font9)
        self.label_2.setFocusPolicy(Qt.TabFocus)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.label_4 = QLabel(self.Title)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setMinimumSize(QSize(720, 0))
        self.label_4.setMaximumSize(QSize(720, 100))
        font10 = QFont()
        font10.setFamilies([u"Roboto"])
        font10.setPointSize(15)
        font10.setBold(False)
        font10.setItalic(True)
        self.label_4.setFont(font10)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)


        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Title)

        self.Frame_btnlogin = QFrame(self.Sigin_form)
        self.Frame_btnlogin.setObjectName(u"Frame_btnlogin")
        self.Frame_btnlogin.setMinimumSize(QSize(720, 60))
        self.Frame_btnlogin.setMaximumSize(QSize(720, 60))
        self.Frame_btnlogin.setFrameShape(QFrame.StyledPanel)
        self.Frame_btnlogin.setFrameShadow(QFrame.Raised)
        self.Signin_btn_login = QPushButton(self.Frame_btnlogin)
        self.Signin_btn_login.setObjectName(u"Signin_btn_login")
        self.Signin_btn_login.setGeometry(QRect(285, 10, 150, 50))
        self.Signin_btn_login.setMinimumSize(QSize(150, 50))
        self.Signin_btn_login.setMaximumSize(QSize(150, 50))
        font11 = QFont()
        font11.setFamilies([u"Roboto"])
        font11.setPointSize(17)
        font11.setBold(False)
        font11.setItalic(False)
        self.Signin_btn_login.setFont(font11)
        self.Signin_btn_login.setFocusPolicy(Qt.WheelFocus)
        self.Signin_btn_login.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(0, 41, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(216, 229, 254);\n"
"	color: rgb(0, 41, 77);\n"
"}")
        self.Signin_btn_login.setAutoDefault(True)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.Frame_btnlogin)

        self.LineEdit_sigin = QFrame(self.Sigin_form)
        self.LineEdit_sigin.setObjectName(u"LineEdit_sigin")
        self.LineEdit_sigin.setMinimumSize(QSize(720, 170))
        self.LineEdit_sigin.setMaximumSize(QSize(720, 170))
        self.LineEdit_sigin.setFrameShape(QFrame.StyledPanel)
        self.LineEdit_sigin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.LineEdit_sigin)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Signin_username = QLineEdit(self.LineEdit_sigin)
        self.Signin_username.setObjectName(u"Signin_username")
        sizePolicy.setHeightForWidth(self.Signin_username.sizePolicy().hasHeightForWidth())
        self.Signin_username.setSizePolicy(sizePolicy)
        self.Signin_username.setMinimumSize(QSize(500, 50))
        self.Signin_username.setMaximumSize(QSize(500, 50))
        font12 = QFont()
        font12.setFamilies([u"Roboto"])
        font12.setPointSize(17)
        font12.setBold(False)
        self.Signin_username.setFont(font12)
        self.Signin_username.setFocusPolicy(Qt.StrongFocus)
        self.Signin_username.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signin_username.setAlignment(Qt.AlignCenter)
        self.Signin_username.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.Signin_username.setClearButtonEnabled(False)

        self.verticalLayout_10.addWidget(self.Signin_username, 0, Qt.AlignHCenter)

        self.Signin_password = QLineEdit(self.LineEdit_sigin)
        self.Signin_password.setObjectName(u"Signin_password")
        sizePolicy.setHeightForWidth(self.Signin_password.sizePolicy().hasHeightForWidth())
        self.Signin_password.setSizePolicy(sizePolicy)
        self.Signin_password.setMinimumSize(QSize(500, 50))
        self.Signin_password.setMaximumSize(QSize(500, 50))
        font13 = QFont()
        font13.setFamilies([u"Roboto"])
        font13.setPointSize(17)
        self.Signin_password.setFont(font13)
        self.Signin_password.setFocusPolicy(Qt.StrongFocus)
        self.Signin_password.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signin_password.setEchoMode(QLineEdit.Password)
        self.Signin_password.setAlignment(Qt.AlignCenter)
        self.Signin_password.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.Signin_password.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.Signin_password, 0, Qt.AlignHCenter)


        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.LineEdit_sigin)


        self.gridLayout_2.addWidget(self.Sigin_form, 0, 0, 1, 1)

        self.Page.addWidget(self.Page_signin)
        self.Page_signup = QWidget()
        self.Page_signup.setObjectName(u"Page_signup")
        self.Page_signup.setStyleSheet(u"background-color: rgb(240, 246, 255);")
        self.gridLayout_3 = QGridLayout(self.Page_signup)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.Signup_form = QFrame(self.Page_signup)
        self.Signup_form.setObjectName(u"Signup_form")
        self.Signup_form.setMaximumSize(QSize(720, 650))
        self.Signup_form.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 41, 77);")
        self.Signup_form.setFrameShape(QFrame.NoFrame)
        self.Signup_form.setFrameShadow(QFrame.Raised)
        self.Signup_form.setLineWidth(5)
        self.formLayout = QFormLayout(self.Signup_form)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, -1, 0)
        self.label_9 = QLabel(self.Signup_form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(720, 70))
        self.label_9.setMaximumSize(QSize(720, 70))
        self.label_9.setFont(font9)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.LineEdit_signup = QFrame(self.Signup_form)
        self.LineEdit_signup.setObjectName(u"LineEdit_signup")
        self.LineEdit_signup.setMinimumSize(QSize(720, 500))
        self.LineEdit_signup.setMaximumSize(QSize(720, 500))
        self.LineEdit_signup.setFrameShape(QFrame.StyledPanel)
        self.LineEdit_signup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.LineEdit_signup)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(110, 0, 0, -1)
        self.Signup_name = QLineEdit(self.LineEdit_signup)
        self.Signup_name.setObjectName(u"Signup_name")
        sizePolicy.setHeightForWidth(self.Signup_name.sizePolicy().hasHeightForWidth())
        self.Signup_name.setSizePolicy(sizePolicy)
        self.Signup_name.setMinimumSize(QSize(500, 50))
        self.Signup_name.setMaximumSize(QSize(500, 50))
        self.Signup_name.setFont(font12)
        self.Signup_name.setFocusPolicy(Qt.StrongFocus)
        self.Signup_name.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_name)

        self.Signup_phone = QLineEdit(self.LineEdit_signup)
        self.Signup_phone.setObjectName(u"Signup_phone")
        sizePolicy.setHeightForWidth(self.Signup_phone.sizePolicy().hasHeightForWidth())
        self.Signup_phone.setSizePolicy(sizePolicy)
        self.Signup_phone.setMinimumSize(QSize(500, 50))
        self.Signup_phone.setMaximumSize(QSize(500, 50))
        self.Signup_phone.setFont(font13)
        self.Signup_phone.setFocusPolicy(Qt.StrongFocus)
        self.Signup_phone.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_phone.setEchoMode(QLineEdit.Normal)
        self.Signup_phone.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_phone)

        self.Signup_username = QLineEdit(self.LineEdit_signup)
        self.Signup_username.setObjectName(u"Signup_username")
        sizePolicy.setHeightForWidth(self.Signup_username.sizePolicy().hasHeightForWidth())
        self.Signup_username.setSizePolicy(sizePolicy)
        self.Signup_username.setMinimumSize(QSize(500, 50))
        self.Signup_username.setMaximumSize(QSize(500, 50))
        self.Signup_username.setFont(font13)
        self.Signup_username.setFocusPolicy(Qt.StrongFocus)
        self.Signup_username.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_username.setEchoMode(QLineEdit.Normal)
        self.Signup_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_username)

        self.Signup_password = QLineEdit(self.LineEdit_signup)
        self.Signup_password.setObjectName(u"Signup_password")
        sizePolicy.setHeightForWidth(self.Signup_password.sizePolicy().hasHeightForWidth())
        self.Signup_password.setSizePolicy(sizePolicy)
        self.Signup_password.setMinimumSize(QSize(500, 50))
        self.Signup_password.setMaximumSize(QSize(500, 50))
        self.Signup_password.setFont(font13)
        self.Signup_password.setFocusPolicy(Qt.StrongFocus)
        self.Signup_password.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_password.setEchoMode(QLineEdit.Password)
        self.Signup_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_password)

        self.Signup_code = QLineEdit(self.LineEdit_signup)
        self.Signup_code.setObjectName(u"Signup_code")
        sizePolicy.setHeightForWidth(self.Signup_code.sizePolicy().hasHeightForWidth())
        self.Signup_code.setSizePolicy(sizePolicy)
        self.Signup_code.setMinimumSize(QSize(500, 50))
        self.Signup_code.setMaximumSize(QSize(500, 50))
        self.Signup_code.setFont(font12)
        self.Signup_code.setFocusPolicy(Qt.StrongFocus)
        self.Signup_code.setStyleSheet(u"background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 41, 77);")
        self.Signup_code.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.Signup_code)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.LineEdit_signup)

        self.Frame_btn_signup = QFrame(self.Signup_form)
        self.Frame_btn_signup.setObjectName(u"Frame_btn_signup")
        self.Frame_btn_signup.setMinimumSize(QSize(720, 80))
        self.Frame_btn_signup.setMaximumSize(QSize(720, 80))
        self.Frame_btn_signup.setFrameShape(QFrame.StyledPanel)
        self.Frame_btn_signup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Frame_btn_signup)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(235, 0, 0, 0)
        self.Signup_btn_signup = QPushButton(self.Frame_btn_signup)
        self.Signup_btn_signup.setObjectName(u"Signup_btn_signup")
        self.Signup_btn_signup.setMinimumSize(QSize(250, 50))
        self.Signup_btn_signup.setMaximumSize(QSize(250, 50))
        self.Signup_btn_signup.setFont(font11)
        self.Signup_btn_signup.setFocusPolicy(Qt.TabFocus)
        self.Signup_btn_signup.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(0, 41, 77);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(216, 229, 254);\n"
"	color: rgb(0, 41, 77);\n"
"}")
        self.Signup_btn_signup.setFlat(True)

        self.verticalLayout_12.addWidget(self.Signup_btn_signup)


        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.Frame_btn_signup)


        self.gridLayout_3.addWidget(self.Signup_form, 0, 0, 1, 1)

        self.Page.addWidget(self.Page_signup)
        self.Page_data = QWidget()
        self.Page_data.setObjectName(u"Page_data")
        self.verticalLayout_13 = QVBoxLayout(self.Page_data)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.menu_data = QFrame(self.Page_data)
        self.menu_data.setObjectName(u"menu_data")
        self.menu_data.setMinimumSize(QSize(0, 100))
        self.menu_data.setMaximumSize(QSize(16777215, 100))
        self.menu_data.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 41, 77);")
        self.menu_data.setFrameShape(QFrame.NoFrame)
        self.menu_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.menu_data)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_30 = QLabel(self.menu_data)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 70))
        self.label_30.setMaximumSize(QSize(16777215, 70))
        font14 = QFont()
        font14.setFamilies([u"Roboto"])
        font14.setPointSize(30)
        font14.setBold(True)
        self.label_30.setFont(font14)
        self.label_30.setStyleSheet(u"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_30)


        self.verticalLayout_13.addWidget(self.menu_data)

        self.data = QFrame(self.Page_data)
        self.data.setObjectName(u"data")
        self.plotdata = QVBoxLayout(self.data)
        self.plotdata.setObjectName(u"plotdata")

        self.verticalLayout_13.addWidget(self.data)

        self.Page.addWidget(self.Page_data)
        self.Page_robotstatus = QWidget()
        self.Page_robotstatus.setObjectName(u"Page_robotstatus")
        self.Page_robotstatus.setEnabled(True)
        self.Page_robotstatus.setMinimumSize(QSize(0, 0))
        self.Page_robotstatus.setMaximumSize(QSize(16777215, 16777215))
        self.Page_robotstatus.setStyleSheet(u"#menu_robotstatus {\n"
"border: 1px solid gray;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.Page_robotstatus)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.menu_robotstatus = QFrame(self.Page_robotstatus)
        self.menu_robotstatus.setObjectName(u"menu_robotstatus")
        self.menu_robotstatus.setMinimumSize(QSize(0, 100))
        self.menu_robotstatus.setMaximumSize(QSize(16777215, 100))
        self.menu_robotstatus.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 41, 77);")
        self.menu_robotstatus.setFrameShape(QFrame.NoFrame)
        self.menu_robotstatus.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.menu_robotstatus)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_29 = QLabel(self.menu_robotstatus)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 70))
        self.label_29.setMaximumSize(QSize(16777215, 70))
        font15 = QFont()
        font15.setFamilies([u"Roboto"])
        font15.setPointSize(30)
        font15.setBold(True)
        font15.setItalic(False)
        font15.setUnderline(False)
        font15.setStrikeOut(False)
        font15.setKerning(True)
        self.label_29.setFont(font15)
        self.label_29.setStyleSheet(u"")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_29)


        self.verticalLayout_5.addWidget(self.menu_robotstatus)

        self.widget_3 = QWidget(self.Page_robotstatus)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.locker = QFrame(self.widget_4)
        self.locker.setObjectName(u"locker")
        self.locker.setMinimumSize(QSize(0, 0))
        self.locker.setMaximumSize(QSize(16777215, 16777215))
        self.locker.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.locker)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.locker)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	border-top-left-radius: 15;\n"
"	border-top-right-radius: 15;\n"
"	border-style: solid;\n"
"	border-color:rgb(0, 41, 77);\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207));\n"
"}")
        self.frame_7.setLineWidth(0)
        self.verticalLayout_23 = QVBoxLayout(self.frame_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label1_3 = QLabel(self.frame_7)
        self.label1_3.setObjectName(u"label1_3")
        font16 = QFont()
        font16.setFamilies([u"Roboto"])
        font16.setPointSize(23)
        font16.setBold(False)
        self.label1_3.setFont(font16)
        self.label1_3.setStyleSheet(u"QLabel{\n"
"background-color: transparent; \n"
"color: rgb(238, 238, 236);\n"
"}")
        self.label1_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label1_3, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.locker)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QSize(16777215, 200))
        self.frame_8.setStyleSheet(u"\n"
"color: rgb(0, 41, 77);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.frame_8.setLineWidth(1)
        self.gridLayout_14 = QGridLayout(self.frame_8)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setVerticalSpacing(4)
        self.gridLayout_14.setContentsMargins(10, 10, 10, 10)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        font17 = QFont()
        font17.setFamilies([u"Roboto"])
        font17.setPointSize(13)
        font17.setBold(True)
        self.label_18.setFont(font17)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(3, 16777215))
        self.label_20.setStyleSheet(u"background-color: rgb(0, 41, 77);")
        self.label_20.setFrameShape(QFrame.StyledPanel)

        self.gridLayout_14.addWidget(self.label_20, 0, 1, 4, 1)

        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font17)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_7, 0, 0, 1, 1)

        self.left_status = QLabel(self.frame_8)
        self.left_status.setObjectName(u"left_status")
        self.left_status.setMinimumSize(QSize(40, 20))
        self.left_status.setMaximumSize(QSize(40, 40))
        self.left_status.setStyleSheet(u"QLabel{\n"
"border-radius: 20px; \n"
"border: 3px solid rgb(0, 41, 77);\n"
"}")
        self.left_status.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.left_status, 1, 0, 1, 1)

        self.right_status = QLabel(self.frame_8)
        self.right_status.setObjectName(u"right_status")
        self.right_status.setMinimumSize(QSize(40, 40))
        self.right_status.setMaximumSize(QSize(40, 40))
        self.right_status.setStyleSheet(u"QLabel{\n"
"border-radius: 20px; \n"
"border: 3px solid rgb(0, 41, 77);\n"
"}")
        self.right_status.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.right_status, 1, 2, 1, 1)


        self.verticalLayout_22.addWidget(self.frame_8)


        self.verticalLayout_14.addWidget(self.locker)

        self.UGV1_2 = QFrame(self.widget_4)
        self.UGV1_2.setObjectName(u"UGV1_2")
        self.UGV1_2.setMinimumSize(QSize(0, 0))
        self.UGV1_2.setMaximumSize(QSize(16777215, 16777215))
        self.UGV1_2.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.UGV1_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.UGV1_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy8)
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	border-top-left-radius: 15;\n"
"	border-top-right-radius: 15;\n"
"	border-style: solid;\n"
"	border-color:rgb(0, 41, 77);\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207));\n"
"}")
        self.frame_6.setLineWidth(0)
        self.verticalLayout_21 = QVBoxLayout(self.frame_6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Robot_label1_2 = QLabel(self.frame_6)
        self.Robot_label1_2.setObjectName(u"Robot_label1_2")
        self.Robot_label1_2.setEnabled(True)
        font18 = QFont()
        font18.setFamilies([u"Roboto"])
        font18.setPointSize(23)
        self.Robot_label1_2.setFont(font18)
        self.Robot_label1_2.setStyleSheet(u"QLabel{\n"
"background-color: transparent; \n"
"color: rgb(238, 238, 236);\n"
"}")

        self.verticalLayout_21.addWidget(self.Robot_label1_2, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.frame_6)


        self.verticalLayout_14.addWidget(self.UGV1_2)


        self.horizontalLayout_9.addWidget(self.widget_4)

        self.frame_4 = QFrame(self.widget_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_4)

        self.UGV1 = QFrame(self.widget_3)
        self.UGV1.setObjectName(u"UGV1")
        sizePolicy.setHeightForWidth(self.UGV1.sizePolicy().hasHeightForWidth())
        self.UGV1.setSizePolicy(sizePolicy)
        self.UGV1.setMinimumSize(QSize(0, 0))
        self.UGV1.setMaximumSize(QSize(16777215, 16777215))
        self.UGV1.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.UGV1)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.UGV1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	border-top-left-radius: 15;\n"
"	border-top-right-radius: 15;\n"
"	border-style: solid;\n"
"	border-color:rgb(0, 41, 77);\n"
"	background-color: qlineargradient(spread: pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(4, 3, 47), stop:0.5 rgb(86, 80, 140), stop:1 rgb(114, 159, 207));\n"
"}")
        self.frame_5.setLineWidth(0)
        self.verticalLayout_19 = QVBoxLayout(self.frame_5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Robot_label1 = QLabel(self.frame_5)
        self.Robot_label1.setObjectName(u"Robot_label1")
        self.Robot_label1.setEnabled(True)
        self.Robot_label1.setFont(font18)
        self.Robot_label1.setStyleSheet(u"QLabel{\n"
"background-color: transparent; \n"
"color: rgb(238, 238, 236);\n"
"}")

        self.verticalLayout_19.addWidget(self.Robot_label1)


        self.verticalLayout_18.addWidget(self.frame_5)


        self.horizontalLayout_9.addWidget(self.UGV1)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.Page.addWidget(self.Page_robotstatus)
        self.Page_tracking = QWidget()
        self.Page_tracking.setObjectName(u"Page_tracking")
        self.Page_tracking.setStyleSheet(u"*{\n"
"background-color: rgb(240, 246, 255);\n"
"}\n"
"#menu_tracking {\n"
"border: 1px solid gray;\n"
"}\n"
"QPushButton{\n"
"border-radius:none;\n"
"color: rgb(186, 189, 182);\n"
"}\n"
"QPushButton:hover{\n"
";\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.Page_tracking)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, 9, 0)
        self.menu_tracking = QFrame(self.Page_tracking)
        self.menu_tracking.setObjectName(u"menu_tracking")
        self.menu_tracking.setMinimumSize(QSize(0, 100))
        self.menu_tracking.setMaximumSize(QSize(16777215, 100))
        self.menu_tracking.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 41, 77);")
        self.menu_tracking.setFrameShape(QFrame.NoFrame)
        self.menu_tracking.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.menu_tracking)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_26 = QLabel(self.menu_tracking)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 70))
        self.label_26.setMaximumSize(QSize(16777215, 70))
        self.label_26.setFont(font14)
        self.label_26.setStyleSheet(u"")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_26)


        self.gridLayout_6.addWidget(self.menu_tracking, 0, 0, 1, 1)

        self.tracking = QVBoxLayout()
        self.tracking.setObjectName(u"tracking")
        self.traking_label = QLabel(self.Page_tracking)
        self.traking_label.setObjectName(u"traking_label")
        self.traking_label.setAlignment(Qt.AlignCenter)
        self.traking_label.setMargin(1)
        self.traking_label.setIndent(1)

        self.tracking.addWidget(self.traking_label)


        self.gridLayout_6.addLayout(self.tracking, 1, 0, 1, 1)

        self.Page.addWidget(self.Page_tracking)
        self.Page_attendance = QWidget()
        self.Page_attendance.setObjectName(u"Page_attendance")
        self.Page_attendance.setStyleSheet(u"*{\n"
"background-color: rgb(240, 246, 255);\n"
"}\n"
"#menu_attendance {\n"
"	border: 1px solid gray;\n"
"} \n"
"#info_frame {\n"
"	border: 1px solid gray;\n"
"} \n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox {\n"
"	padding: 4px 5px;\n"
"	border: 1px solid #838383;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"#info_frame QLineEdit:focus,\n"
"#info_frame QComboBox:focus\n"
" {\n"
"	border-color: #0055ff;\n"
"}\n"
"\n"
"QComboBox::drop-down { \n"
"	background: transparent; \n"
"	border: none;\n"
"	margin-right: 5px;\n"
"} \n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/icons/icons/expand_more.svg);\n"
"}\n"
"\n"
"#info_frame QPushButton {\n"
"	font-size: 14px;\n"
"	padding: 5px 10px;\n"
"	border: 2px solid #f0f0f0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#info_frame QPushButton:hover {\n"
"	border-color: #4c96f7;\n"
"	font-size: 15px;\n"
"}\n"
"#result_frame {\n"
"	border-radius: 5px;\n"
"}\n"
"QTableWidget::Item{\n"
"	border-bottom:1px solid #d0c6ff;\n"
"	color: black;\n"
"	padding-left: 3px;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.Page_attendance)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.Page_attendance)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_15 = QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.menu_attendance = QWidget(self.widget_2)
        self.menu_attendance.setObjectName(u"menu_attendance")
        self.menu_attendance.setMinimumSize(QSize(0, 100))
        self.menu_attendance.setMaximumSize(QSize(16777215, 100))
        self.menu_attendance.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 41, 77);")
        self.horizontalLayout_5 = QHBoxLayout(self.menu_attendance)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_28 = QLabel(self.menu_attendance)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setEnabled(True)
        self.label_28.setMinimumSize(QSize(0, 70))
        self.label_28.setMaximumSize(QSize(16777215, 100))
        self.label_28.setBaseSize(QSize(0, 70))
        self.label_28.setFont(font14)
        self.label_28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.label_28.setFrameShape(QFrame.StyledPanel)
        self.label_28.setFrameShadow(QFrame.Sunken)
        self.label_28.setMidLineWidth(5)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_28)


        self.verticalLayout_15.addWidget(self.menu_attendance)

        self.info_frame = QFrame(self.widget_2)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMaximumSize(QSize(16777215, 200))
        font19 = QFont()
        font19.setFamilies([u"Roboto"])
        font19.setPointSize(16)
        font19.setBold(False)
        self.info_frame.setFont(font19)
        self.info_frame.setStyleSheet(u"border-radius: 20px;\n"
"color: rgb(0, 41, 77);")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.info_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setContentsMargins(20, 0, 20, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(20)
        self.label = QLabel(self.info_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font20 = QFont()
        font20.setFamilies([u"Roboto"])
        font20.setPointSize(12)
        font20.setBold(False)
        self.label.setFont(font20)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.info_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 50))
        self.label_3.setFont(font20)

        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.info_frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy9)
        self.lineEdit_2.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.info_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy9.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy9)
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        self.lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)

        self.gridLayout_11.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.search_btn = QPushButton(self.info_frame)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy6.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy6)
        self.search_btn.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(20, 20))

        self.gridLayout_9.addWidget(self.search_btn, 0, 2, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(10)
        self.gridLayout_10.setVerticalSpacing(20)
        self.label_6 = QLabel(self.info_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font20)

        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.info_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setFont(font20)

        self.gridLayout_10.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.info_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy9)
        self.lineEdit_3.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_10.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.info_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy9)
        self.lineEdit_4.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_10.addWidget(self.lineEdit_4, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.info_frame)

        self.result_frame = QFrame(self.widget_2)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setMaximumSize(QSize(16777215, 625))
        self.result_frame.setStyleSheet(u"\n"
"color: rgb(0, 41, 77);")
        self.gridLayout_8 = QGridLayout(self.result_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_attendance = QTableWidget(self.result_frame)
        if (self.table_attendance.columnCount() < 6):
            self.table_attendance.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font7);
        self.table_attendance.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font21 = QFont()
        font21.setFamilies([u"Roboto"])
        font21.setPointSize(11)
        font21.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font21);
        self.table_attendance.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font7);
        self.table_attendance.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font7);
        self.table_attendance.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font7);
        self.table_attendance.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem5.setFont(font7);
        self.table_attendance.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_attendance.setObjectName(u"table_attendance")
        font22 = QFont()
        font22.setFamilies([u"Roboto"])
        font22.setPointSize(11)
        self.table_attendance.setFont(font22)
        self.table_attendance.setFocusPolicy(Qt.NoFocus)
        self.table_attendance.setStyleSheet(u"")
        self.table_attendance.setFrameShape(QFrame.NoFrame)
        self.table_attendance.setFrameShadow(QFrame.Raised)
        self.table_attendance.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_attendance.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_attendance.setShowGrid(False)
        self.table_attendance.setGridStyle(Qt.NoPen)
        self.table_attendance.setSortingEnabled(True)
        self.table_attendance.setWordWrap(True)
        self.table_attendance.setCornerButtonEnabled(False)
        self.table_attendance.setRowCount(0)
        self.table_attendance.setColumnCount(6)
        self.table_attendance.horizontalHeader().setCascadingSectionResizes(False)
        self.table_attendance.horizontalHeader().setMinimumSectionSize(50)
        self.table_attendance.horizontalHeader().setDefaultSectionSize(120)
        self.table_attendance.horizontalHeader().setHighlightSections(True)
        self.table_attendance.horizontalHeader().setStretchLastSection(True)
        self.table_attendance.verticalHeader().setVisible(False)
        self.table_attendance.verticalHeader().setCascadingSectionResizes(False)
        self.table_attendance.verticalHeader().setMinimumSectionSize(30)
        self.table_attendance.verticalHeader().setDefaultSectionSize(30)
        self.table_attendance.verticalHeader().setHighlightSections(False)
        self.table_attendance.verticalHeader().setProperty(u"showSortIndicator", True)
        self.table_attendance.verticalHeader().setStretchLastSection(False)

        self.gridLayout_8.addWidget(self.table_attendance, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.result_frame)


        self.horizontalLayout_6.addWidget(self.widget_2)

        self.Page.addWidget(self.Page_attendance)
        self.Page_Camera = QWidget()
        self.Page_Camera.setObjectName(u"Page_Camera")
        self.Page_Camera.setStyleSheet(u"*{\n"
"background-color: rgb(240, 246, 255);\n"
"}\n"
"QPushButton{\n"
"border-radius:none;\n"
"color: rgb(186, 189, 182);\n"
"}\n"
"QPushButton:hover{\n"
";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#menu_camera {\n"
"	border: 1px solid gray;\n"
"} ")
        self.gridLayout_7 = QGridLayout(self.Page_Camera)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.menu_camera = QFrame(self.Page_Camera)
        self.menu_camera.setObjectName(u"menu_camera")
        self.menu_camera.setMinimumSize(QSize(0, 100))
        self.menu_camera.setMaximumSize(QSize(16777215, 100))
        self.menu_camera.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"color: rgb(0, 41, 77);\n"
"")
        self.menu_camera.setFrameShape(QFrame.NoFrame)
        self.menu_camera.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.menu_camera)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_27 = QLabel(self.menu_camera)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 70))
        self.label_27.setMaximumSize(QSize(16777215, 100))
        self.label_27.setFont(font15)
        self.label_27.setStyleSheet(u"")
        self.label_27.setFrameShape(QFrame.StyledPanel)
        self.label_27.setFrameShadow(QFrame.Sunken)
        self.label_27.setMidLineWidth(5)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_27)


        self.gridLayout_7.addWidget(self.menu_camera, 0, 0, 1, 1)

        self.camera = QVBoxLayout()
        self.camera.setObjectName(u"camera")
        self.camera_label = QLabel(self.Page_Camera)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setScaledContents(False)
        self.camera_label.setAlignment(Qt.AlignCenter)

        self.camera.addWidget(self.camera_label)


        self.gridLayout_7.addLayout(self.camera, 1, 0, 1, 1)

        self.Page.addWidget(self.Page_Camera)

        self.verticalLayout_16.addWidget(self.Page)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Main_btn_tracking, self.Signin_btn_signin)
        QWidget.setTabOrder(self.Signin_btn_signin, self.Signin_btn_signup)

        self.retranslateUi(MainWindow)

        self.Dashboard.setCurrentIndex(1)
        self.Main_btn_attendance.setDefault(True)
        self.Main_btn_camera.setDefault(True)
        self.Main_btn_tracking.setDefault(True)
        self.Main_btn_robotstatus.setDefault(True)
        self.Account__btnlogout.setDefault(True)
        self.Page.setCurrentIndex(2)
        self.Signin_btn_login.setDefault(True)
        self.Signup_btn_signup.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Robot Management", None))
        self.Logo_BK.setText("")
        self.Logo_fab.setText("")
        self.Signin_btn_signin.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.Signin_btn_signup.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.Signin_text.setText(QCoreApplication.translate("MainWindow", u"FAB-LAB \n"
" All rights reserved", None))
        self.Logo_BK_2.setText("")
        self.Logo_fab_2.setText("")
        self.Label_admin.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.Main_btn_attendance.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        self.Main_btn_camera.setText(QCoreApplication.translate("MainWindow", u"CAMERA", None))
        self.Main_btn_tracking.setText(QCoreApplication.translate("MainWindow", u"TRACKING", None))
        self.Main_btn_robotstatus.setText(QCoreApplication.translate("MainWindow", u"ROBOT STATUS", None))
        self.Main_btn_data.setText(QCoreApplication.translate("MainWindow", u"LIVE TELEMETRY ", None))
        self.Account_username.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.Account__btnlogout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.label_8.setText("")
        self.label_mqtt.setText(QCoreApplication.translate("MainWindow", u"connected", None))
        self.label_battery.setText(QCoreApplication.translate("MainWindow", u"battery", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Please enter your username and password", None))
        self.Signin_btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Signin_username.setText("")
        self.Signin_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Signin_password.setText("")
        self.Signin_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"SIGN UP", None))
        self.Signup_name.setText("")
        self.Signup_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full name", None))
        self.Signup_phone.setText("")
        self.Signup_phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone number", None))
        self.Signup_username.setText("")
        self.Signup_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Signup_password.setText("")
        self.Signup_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Signup_code.setText("")
        self.Signup_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Verify code", None))
        self.Signup_btn_signup.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"LIVE TELEMETRY ", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ROBOT STATUS", None))
        self.label1_3.setText(QCoreApplication.translate("MainWindow", u"	LOCKER", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.label_20.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.left_status.setText("")
        self.right_status.setText("")
        self.Robot_label1_2.setText(QCoreApplication.translate("MainWindow", u"tobecontinue", None))
        self.Robot_label1.setText(QCoreApplication.translate("MainWindow", u"tobecontinue", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TRACKING", None))
        self.traking_label.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"ATTENDANCE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.search_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email Address", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        ___qtablewidgetitem = self.table_attendance.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None));
        ___qtablewidgetitem1 = self.table_attendance.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table_attendance.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem3 = self.table_attendance.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.table_attendance.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Check-in Time", None));
        ___qtablewidgetitem5 = self.table_attendance.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Email Address", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"CAMERA", None))
        self.camera_label.setText("")
    # retranslateUi

