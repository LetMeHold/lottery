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
        MainWindow.resize(1119, 800)
        MainWindow.setStyleSheet("border-image: url(:/1/bg.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labShow = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labShow.sizePolicy().hasHeightForWidth())
        self.labShow.setSizePolicy(sizePolicy)
        self.labShow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labShow.setFont(font)
        self.labShow.setStyleSheet("border-image: url();")
        self.labShow.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labShow.setObjectName("labShow")
        self.horizontalLayout.addWidget(self.labShow)
        self.labName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labName.sizePolicy().hasHeightForWidth())
        self.labName.setSizePolicy(sizePolicy)
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
        self.labHelp = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labHelp.sizePolicy().hasHeightForWidth())
        self.labHelp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(13)
        self.labHelp.setFont(font)
        self.labHelp.setStyleSheet("border-image: url();")
        self.labHelp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labHelp.setObjectName("labHelp")
        self.horizontalLayout.addWidget(self.labHelp)
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
        self.labHelp.setText(_translate("MainWindow", "h - 显示/隐藏该帮助信息\n"
"enter - 开始/结束抽奖\n"
"space - 开始/结束抽奖\n"
"backspace - 重置数据\n"
"delete - 重置数据\n"
"f11 - 全屏显示\n"
"esc - 退出全屏"))

import bg_rc
