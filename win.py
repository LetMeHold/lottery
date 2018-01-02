# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from lottery import *
from gl import *
import random
from PyQt5.QtCore import QTimer,Qt

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #self.relate()
        self.data = loadJsonFile("data.json")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.draw)

    def draw(self):
        name = random.choice(self.data['actor'])
        self.labName.setText(name)

    def start(self):
        self.timer.start(self.data['refresh'])

    def stop(self):
        self.timer.stop()
        self.labName.setText('李昱平')

    #def relate(self):
        #self.btnStart.clicked.connect(self.start)
        #self.btnStop.clicked.connect(self.stop)

    def keyPressEvent(self, e):
        #if e.key() == QtCore.Qt.Key_Escape:
        if e.key()==Qt.Key_Return or e.key()==Qt.Key_Space:
            if self.timer.isActive():
                self.stop()
            else:
                self.start()
        elif e.key() == Qt.Key_F11:
            self.showFullScreen()
        elif e.key() == Qt.Key_Escape:
            self.showNormal()


