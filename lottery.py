# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lottery.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 708)
        MainWindow.setStyleSheet("border-image: url(:/1/bg.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labShow = QtWidgets.QLabel(self.centralwidget)
        self.labShow.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labShow.setFont(font)
        self.labShow.setStyleSheet("border-image: url();")
        self.labShow.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labShow.setObjectName("labShow")
        self.horizontalLayout.addWidget(self.labShow)
        self.labName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(88)
        font.setBold(True)
        font.setWeight(75)
        self.labName.setFont(font)
        self.labName.setStyleSheet("border-image: url();")
        self.labName.setAlignment(QtCore.Qt.AlignCenter)
        self.labName.setObjectName("labName")
        self.horizontalLayout.addWidget(self.labName)
        spacerItem = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "万泊科技抽奖程序"))
        self.labShow.setText(_translate("MainWindow", "一等奖, {prize1}\n"
"{winner1.1}\n"
"\n"
"二等奖, {prize2}\n"
"{winner2.1}\n"
"{winner2.2}\n"
"\n"
"三等奖, {prize3}\n"
"{winner3.1}\n"
"{winner3.2}\n"
"{winner3.3}"))
        self.labName.setText(_translate("MainWindow", "无名氏"))

import bg_rc
