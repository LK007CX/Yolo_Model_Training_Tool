#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MapWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(MapWidget, self).__init__(*args, **kwargs)
        
        self.label = QLabel("Map", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MapWidget()
    win.show()
    sys.exit(app.exec_())