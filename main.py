# -*- coding: utf-8 -*-
# pyrcc5 -o bg_rc.py bg.qrc
# pyuic5.bat -o lottery.py lottery.ui
# pyinstaller -F -w main.py -n lottery

from PyQt5.QtWidgets import QApplication
from win import *

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

