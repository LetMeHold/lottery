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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.verticalLayout.addWidget(self.labName)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labName.setText(_translate("MainWindow", "无名氏"))

import bg_rc
