#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QSplashScreen, QWidget, QLabel


"""
启动SplashScreen
"""


class GifSplashScreen(QSplashScreen):

    def __init__(self, *args, **kwargs):
        super(GifSplashScreen, self).__init__(*args, **kwargs)
        self.movie = QMovie('image/splash.gif')
        self.movie.frameChanged.connect(self.onFrameChanged)
        self.movie.start()

    def onFrameChanged(self, _):
        self.setPixmap(self.movie.currentPixmap())

    def finish(self, widget):
        self.movie.stop()
        super(GifSplashScreen, self).finish(widget)