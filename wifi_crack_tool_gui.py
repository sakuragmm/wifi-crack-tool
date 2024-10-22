# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wifi_crack_tool_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(529, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(529, 600))
        icon = QIcon()
        icon.addFile(u"images/wificrack.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(529, 500))
        self.lbl_wifi_name = QLabel(self.centralwidget)
        self.lbl_wifi_name.setObjectName(u"lbl_wifi_name")
        self.lbl_wifi_name.setGeometry(QRect(50, 10, 71, 20))
        self.cbo_wifi_name = QComboBox(self.centralwidget)
        self.cbo_wifi_name.setObjectName(u"cbo_wifi_name")
        self.cbo_wifi_name.setGeometry(QRect(120, 10, 201, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbo_wifi_name.sizePolicy().hasHeightForWidth())
        self.cbo_wifi_name.setSizePolicy(sizePolicy1)
        self.cbo_wifi_name.setMinimumSize(QSize(201, 22))
        self.cbo_wifi_name.setMaximumSize(QSize(201, 22))
        self.cbo_wifi_name.setEditable(True)
        self.lbl_security_type = QLabel(self.centralwidget)
        self.lbl_security_type.setObjectName(u"lbl_security_type")
        self.lbl_security_type.setGeometry(QRect(50, 40, 71, 20))
        self.cbo_security_type = QComboBox(self.centralwidget)
        self.cbo_security_type.setObjectName(u"cbo_security_type")
        self.cbo_security_type.setGeometry(QRect(120, 40, 201, 22))
        sizePolicy1.setHeightForWidth(self.cbo_security_type.sizePolicy().hasHeightForWidth())
        self.cbo_security_type.setSizePolicy(sizePolicy1)
        self.cbo_security_type.setMinimumSize(QSize(201, 22))
        self.cbo_security_type.setMaximumSize(QSize(201, 22))
        self.lbl_wnic = QLabel(self.centralwidget)
        self.lbl_wnic.setObjectName(u"lbl_wnic")
        self.lbl_wnic.setGeometry(QRect(50, 70, 71, 20))
        self.cbo_wnic = QComboBox(self.centralwidget)
        self.cbo_wnic.setObjectName(u"cbo_wnic")
        self.cbo_wnic.setGeometry(QRect(120, 70, 352, 22))
        sizePolicy1.setHeightForWidth(self.cbo_wnic.sizePolicy().hasHeightForWidth())
        self.cbo_wnic.setSizePolicy(sizePolicy1)
        self.cbo_wnic.setMinimumSize(QSize(201, 22))
        self.cbo_wnic.setMaximumSize(QSize(352, 22))
        self.lbl_using_pwd_file = QLabel(self.centralwidget)
        self.lbl_using_pwd_file.setObjectName(u"lbl_using_pwd_file")
        self.lbl_using_pwd_file.setGeometry(QRect(5, 100, 521, 16))
        self.lbl_using_pwd_file.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_log_msg_info = QTextEdit(self.centralwidget)
        self.txt_log_msg_info.setObjectName(u"txt_log_msg_info")
        self.txt_log_msg_info.setGeometry(QRect(0, 150, 529, 350))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(100, 120, 331, 24))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.btn_change_pwd_file = QPushButton(self.splitter)
        self.btn_change_pwd_file.setObjectName(u"btn_change_pwd_file")
        self.splitter.addWidget(self.btn_change_pwd_file)
        self.btn_refresh_wifi = QPushButton(self.splitter)
        self.btn_refresh_wifi.setObjectName(u"btn_refresh_wifi")
        self.splitter.addWidget(self.btn_refresh_wifi)
        self.btn_start = QPushButton(self.splitter)
        self.btn_start.setObjectName(u"btn_start")
        self.splitter.addWidget(self.btn_start)
        self.btn_stop = QPushButton(self.splitter)
        self.btn_stop.setObjectName(u"btn_stop")
        self.splitter.addWidget(self.btn_stop)
        self.lbl_scan_time = QLabel(self.centralwidget)
        self.lbl_scan_time.setObjectName(u"lbl_scan_time")
        self.lbl_scan_time.setGeometry(QRect(330, 10, 81, 20))
        self.dbl_scan_time = QDoubleSpinBox(self.centralwidget)
        self.dbl_scan_time.setObjectName(u"dbl_scan_time")
        self.dbl_scan_time.setGeometry(QRect(410, 10, 62, 22))
        self.dbl_scan_time.setDecimals(1)
        self.dbl_scan_time.setMinimum(0.100000000000000)
        self.dbl_scan_time.setSingleStep(0.100000000000000)
        self.dbl_scan_time.setValue(8.000000000000000)
        self.lbl_connect_time = QLabel(self.centralwidget)
        self.lbl_connect_time.setObjectName(u"lbl_connect_time")
        self.lbl_connect_time.setGeometry(QRect(330, 40, 81, 20))
        self.dbl_connect_time = QDoubleSpinBox(self.centralwidget)
        self.dbl_connect_time.setObjectName(u"dbl_connect_time")
        self.dbl_connect_time.setGeometry(QRect(410, 40, 62, 22))
        self.dbl_connect_time.setDecimals(1)
        self.dbl_connect_time.setMinimum(0.100000000000000)
        self.dbl_connect_time.setSingleStep(0.100000000000000)
        self.dbl_connect_time.setValue(3.000000000000000)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WiFi\u5bc6\u7801\u66b4\u529b\u7834\u89e3\u5de5\u5177v1.2.4", None))
        self.lbl_wifi_name.setText(QCoreApplication.translate("MainWindow", u"WiFi\u540d\u79f0:", None))
        self.lbl_security_type.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u5168\u7c7b\u578b:", None))
        self.lbl_wnic.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u7ebf\u7f51\u5361:", None))
        self.lbl_using_pwd_file.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u4f7f\u7528\u5bc6\u7801\u672c: ", None))
        self.btn_change_pwd_file.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u6362\u5bc6\u7801\u672c", None))
        self.btn_refresh_wifi.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cfWiFi", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.lbl_scan_time.setText(QCoreApplication.translate("MainWindow", u"\u626b\u63cf\u65f6\u95f4(s):", None))
        self.lbl_connect_time.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65f6\u95f4(s):", None))
    # retranslateUi

