#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


"""
2.导入标注
"""


class TaggingWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TaggingWidget, self).__init__(*args, **kwargs)

        self.imageLabel = QLabel()

        self.prevPushButton = QPushButton()
        self.nextPushButton = QPushButton()

        self.initUI()

        topLeftLayout = QHBoxLayout()
        topLeftLayout.addWidget(self.imageLabel)

        bottomLeftLayout = QHBoxLayout()
        bottomLeftLayout.addStretch(1)
        bottomLeftLayout.addWidget(self.prevPushButton)
        bottomLeftLayout.addWidget(self.nextPushButton)
        bottomLeftLayout.addStretch(1)

        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addLayout(bottomLeftLayout)

        rightLayout = QVBoxLayout()

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        self.setLayout(layout)
    
    def initUI(self):
        self.imageLabel.setPixmap(QPixmap('image/darknet.png'))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setMaximumSize(QSize(960, 540))
        self.prevPushButton.setIcon(QIcon('image/prev.png'))
        self.prevPushButton.setMinimumSize(QSize(100, 50))
        self.prevPushButton.setIconSize(QSize(45, 45))
        # self.prevPushButton.setStyleSheet()
        self.nextPushButton.setIcon(QIcon('image/next.png'))
        self.nextPushButton.setMinimumSize(QSize(100, 50))
        self.nextPushButton.setIconSize(QSize(45, 45))




class FileChooseWidget(QWidget):

    def __init__(self, name, item, ):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TaggingWidget()
    win.show()
    sys.exit(app.exec_())


