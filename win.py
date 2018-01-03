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
        self.showMaximized()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.draw)

    def initdata(self):
        self.labName.setText('')
        self.data = loadJsonFile('data.json')
        self.info = ''
        itm = self.data['lottery'].items()
        itm = sorted(itm,reverse=True)
        for k,v in itm:
            title = '%s, %s' % (v['name'], v['prize'])
            winners = ''
            for i in range(1,v['time']+1):
                tmp = ''
                for j in range(1, v['amount']+1):
                    if j == 1:
                        tmp += '%s.%d.%d 待定' % (k,i,j)
                    else:
                        tmp += '、%s.%d.%d 待定' % (k,i,j)
                winners += '%s\n' % tmp
            self.info += '%s\n%s\n' % (title,winners)
        lty = self.data['progress']['lottery']
        tm = self.data['progress']['time']
        self.showinfo(self.progress(lty,tm), self.info)

    def progress(self, lty, tm):  #获取最新进度消息
        if lty == 0:
            return '本次抽奖已全部结束'
        return '进度: %s, 第%d次, 抽%d人' % (
            self.data['lottery'][str(lty)]['name'], \
            tm,
            self.data['lottery'][str(lty)]['amount'])

    def showinfo(self, progress, info):
        self.labShow.setText('%s\n\n%s' % (progress,info))

    def draw(self):
        name = random.choice(self.data['actor'])
        self.labName.setText(name)

    def start(self):
        lty = self.data['progress']['lottery']
        if lty == 0:    #表示抽奖已全部结束
            self.showinfo(self.progress(0,0), self.info)
            self.labName.setText('谢谢')
            return
            #lty = len(self.data['lottery'])
            #self.data['progress']['lottery'] = lty
            #self.data['progress']['time'] = self.data['lottery'][str(lty)]['time']
        tm = self.data['progress']['time']
        self.showinfo(self.progress(lty,tm), self.info)
        self.timer.start(self.data['refresh'])

    def stop(self):
        self.timer.stop()
        lty = self.data['progress']['lottery']
        tm = self.data['progress']['time']
        if tm == self.data['lottery'][str(lty)]['time']:
            self.data['progress']['lottery'] -= 1
            self.data['progress']['time'] = 1
        else:
            self.data['progress']['time'] += 1

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
            #self.showNormal()
            self.showMaximized()


