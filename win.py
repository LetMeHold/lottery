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
        self.initdata()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.draw)

    def initdata(self):
        self.labName.setText('')
        self.data = loadJsonFile('data.json')
        info = ''
        itm = self.data['lottery'].items()
        itm = sorted(itm)
        for k,v in itm:
            title = '%s, %s' % (v['name'], v['prize'])
            winners = ''
            for i in range(1,v['time']+1):
                tmp = None
                for j in range(1, v['amount']+1):
                    if j == 1:
                        tmp = '%d.%d 待定' % (i,j)
                    else:
                        tmp = '、%d.%d 待定' % (i,j)
                    tmp = '%s.%s' % (k,tmp)
                winners += '%s\n' % tmp
            info += '%s\n%s\n' % (title,winners)
        self.labShow.setText(info)

    def draw(self):
        name = random.choice(self.data['actor'])
        self.labName.setText(name)

    def start(self):
        self.timer.start(self.data['refresh'])

    def stop(self):
        self.timer.stop()

    #def relate(self):
        #self.btnStart.clicked.connect(self.start)
        #self.btnStop.clicked.connect(self.stop)

    def keyPressEvent(self, e):
        if e.key()==Qt.Key_Return or e.key()==Qt.Key_Space:
            if self.timer.isActive():
                self.stop()
            else:
                self.start()
        elif e.key() == Qt.Key_F11:
            self.showFullScreen()
        elif e.key() == Qt.Key_Escape:
            self.showNormal()


