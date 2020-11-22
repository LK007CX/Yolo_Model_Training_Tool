#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
sys.path.append('./ui')
from ui.GifSplashScreen import GifSplashScreen
from ui.MainWidget import Winform
import qdarkstyle


if __name__ == '__main__':
    import sys
    import cgitb

    cgitb.enable(1, None, 5, '')
    app = QApplication(sys.argv)
    splash = GifSplashScreen()
    splash.show()

    def createWindow():
        app.w = Winform()
        # 模拟初始n秒后再显示
        splash.showMessage('等待界面显示', Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
        QTimer.singleShot(50, lambda: (
            splash.showMessage('初始化完成', Qt.AlignHCenter | Qt.AlignBottom, Qt.white), app.w.show(),
            splash.finish(app.w)))


    # 模拟耗时n秒。但是不能用sleep
    # 可以使用子线程加载耗时的数据
    # 主线程中循环设置UI可以配合QApplication.instance().processEvents()
    splash.showMessage('等待创建界面', Qt.AlignHCenter | Qt.AlignBottom, Qt.white)
    QTimer.singleShot(50, createWindow)

    sys.exit(app.exec_())