# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openithm.ui',
# licensing of 'openithm.ui' applies.
#
# Created: Mon Feb 18 13:43:30 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(9, 10, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 301, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.touchboardLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.touchboardLayout.setSpacing(0)
        self.touchboardLayout.setContentsMargins(-1, -1, -1, 0)
        self.touchboardLayout.setObjectName("touchboardLayout")
        self.tlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.tlabel.setFont(font)
        self.tlabel.setObjectName("tlabel")
        self.touchboardLayout.addWidget(self.tlabel)
        self.tthreshold = QtWidgets.QHBoxLayout()
        self.tthreshold.setSpacing(10)
        self.tthreshold.setContentsMargins(10, -1, 10, -1)
        self.tthreshold.setObjectName("tthreshold")
        self.thres_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.thres_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.thres_label.setObjectName("thres_label")
        self.tthreshold.addWidget(self.thres_label)
        self.thres_val = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.thres_val.setObjectName("thres_val")
        self.tthreshold.addWidget(self.thres_val)
        self.thres_current = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.thres_current.setObjectName("thres_current")
        self.tthreshold.addWidget(self.thres_current)
        self.touchboardLayout.addLayout(self.tthreshold)
        self.tdead_zone = QtWidgets.QHBoxLayout()
        self.tdead_zone.setSpacing(10)
        self.tdead_zone.setContentsMargins(10, -1, 10, -1)
        self.tdead_zone.setObjectName("tdead_zone")
        self.dead_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dead_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.dead_label.setObjectName("dead_label")
        self.tdead_zone.addWidget(self.dead_label)
        self.dead_val = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.dead_val.setObjectName("dead_val")
        self.tdead_zone.addWidget(self.dead_val)
        self.dead_current = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dead_current.setObjectName("dead_current")
        self.tdead_zone.addWidget(self.dead_current)
        self.touchboardLayout.addLayout(self.tdead_zone)
        self.talpha = QtWidgets.QHBoxLayout()
        self.talpha.setSpacing(10)
        self.talpha.setContentsMargins(10, -1, 10, -1)
        self.talpha.setObjectName("talpha")
        self.alpha_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.alpha_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.alpha_label.setObjectName("alpha_label")
        self.talpha.addWidget(self.alpha_label)
        self.alpha_val = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.alpha_val.setObjectName("alpha_val")
        self.talpha.addWidget(self.alpha_val)
        self.alpha_current = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.alpha_current.setObjectName("alpha_current")
        self.talpha.addWidget(self.alpha_current)
        self.touchboardLayout.addLayout(self.talpha)
        self.tbuttons = QtWidgets.QHBoxLayout()
        self.tbuttons.setSpacing(10)
        self.tbuttons.setContentsMargins(-1, 5, -1, -1)
        self.tbuttons.setObjectName("tbuttons")
        self.tapply = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.tapply.setObjectName("tapply")
        self.tbuttons.addWidget(self.tapply)
        self.tcalibrate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.tcalibrate.setObjectName("tcalibrate")
        self.tbuttons.addWidget(self.tcalibrate)
        self.touchboardLayout.addLayout(self.tbuttons)
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(169, 10, 141, 20))
        self.status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status.setObjectName("status")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 301, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.irLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.irLayout.setSpacing(0)
        self.irLayout.setContentsMargins(-1, -1, -1, 0)
        self.irLayout.setObjectName("irLayout")
        self.irlabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.irlabel.setFont(font)
        self.irlabel.setObjectName("irlabel")
        self.irLayout.addWidget(self.irlabel)
        self.irdead_zone = QtWidgets.QHBoxLayout()
        self.irdead_zone.setSpacing(10)
        self.irdead_zone.setContentsMargins(10, -1, 10, -1)
        self.irdead_zone.setObjectName("irdead_zone")
        self.irdead_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.irdead_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.irdead_label.setObjectName("irdead_label")
        self.irdead_zone.addWidget(self.irdead_label)
        self.irdead_val = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.irdead_val.setObjectName("irdead_val")
        self.irdead_zone.addWidget(self.irdead_val)
        self.irdead_current = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.irdead_current.setObjectName("irdead_current")
        self.irdead_zone.addWidget(self.irdead_current)
        self.irLayout.addLayout(self.irdead_zone)
        self.iralpha = QtWidgets.QHBoxLayout()
        self.iralpha.setSpacing(10)
        self.iralpha.setContentsMargins(10, -1, 10, -1)
        self.iralpha.setObjectName("iralpha")
        self.iralpha_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.iralpha_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.iralpha_label.setObjectName("iralpha_label")
        self.iralpha.addWidget(self.iralpha_label)
        self.iralpha_val = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.iralpha_val.setObjectName("iralpha_val")
        self.iralpha.addWidget(self.iralpha_val)
        self.iralpha_current = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.iralpha_current.setObjectName("iralpha_current")
        self.iralpha.addWidget(self.iralpha_current)
        self.irLayout.addLayout(self.iralpha)
        self.irbuttons = QtWidgets.QHBoxLayout()
        self.irbuttons.setSpacing(10)
        self.irbuttons.setContentsMargins(-1, 5, -1, -1)
        self.irbuttons.setObjectName("irbuttons")
        self.irapply = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.irapply.setObjectName("irapply")
        self.irbuttons.addWidget(self.irapply)
        self.ircalibrate = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ircalibrate.setObjectName("ircalibrate")
        self.irbuttons.addWidget(self.ircalibrate)
        self.irLayout.addLayout(self.irbuttons)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 320, 301, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.otherbuttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.otherbuttons.setContentsMargins(0, 0, 0, 0)
        self.otherbuttons.setObjectName("otherbuttons")
        self.about = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.about.setObjectName("about")
        self.otherbuttons.addWidget(self.about)
        self.pause = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pause.setObjectName("pause")
        self.otherbuttons.addWidget(self.pause)
        self.resume = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.resume.setObjectName("resume")
        self.otherbuttons.addWidget(self.resume)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "OpeNITHM", None, -1))
        self.title.setText(QtWidgets.QApplication.translate("MainWindow", "OpeNITHM Config", None, -1))
        self.tlabel.setText(QtWidgets.QApplication.translate("MainWindow", "Touchboard", None, -1))
        self.thres_label.setText(QtWidgets.QApplication.translate("MainWindow", "Threshold", None, -1))
        self.thres_current.setText(QtWidgets.QApplication.translate("MainWindow", "Current: 0", None, -1))
        self.dead_label.setText(QtWidgets.QApplication.translate("MainWindow", "Dead Zone", None, -1))
        self.dead_current.setText(QtWidgets.QApplication.translate("MainWindow", "Current: 0", None, -1))
        self.alpha_label.setText(QtWidgets.QApplication.translate("MainWindow", "Alpha", None, -1))
        self.alpha_current.setText(QtWidgets.QApplication.translate("MainWindow", "Current: 0.00", None, -1))
        self.tapply.setText(QtWidgets.QApplication.translate("MainWindow", "Apply", None, -1))
        self.tcalibrate.setText(QtWidgets.QApplication.translate("MainWindow", "Calibrate Keys", None, -1))
        self.status.setText(QtWidgets.QApplication.translate("MainWindow", "Status: Not Connected", None, -1))
        self.irlabel.setText(QtWidgets.QApplication.translate("MainWindow", "IR Sensors", None, -1))
        self.irdead_label.setText(QtWidgets.QApplication.translate("MainWindow", "Dead Zone", None, -1))
        self.irdead_current.setText(QtWidgets.QApplication.translate("MainWindow", "Current: 0", None, -1))
        self.iralpha_label.setText(QtWidgets.QApplication.translate("MainWindow", "Alpha", None, -1))
        self.iralpha_current.setText(QtWidgets.QApplication.translate("MainWindow", "Current: 0.00", None, -1))
        self.irapply.setText(QtWidgets.QApplication.translate("MainWindow", "Apply", None, -1))
        self.ircalibrate.setText(QtWidgets.QApplication.translate("MainWindow", "Recalibrate", None, -1))
        self.about.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.pause.setText(QtWidgets.QApplication.translate("MainWindow", "Pause", None, -1))
        self.resume.setText(QtWidgets.QApplication.translate("MainWindow", "Resume", None, -1))
