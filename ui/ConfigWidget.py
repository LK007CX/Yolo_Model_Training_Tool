#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


"""
3.
"""


class ConfigWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(ConfigWidget, self).__init__(*args, **kwargs)
        
        self.label = QLabel("Config", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ConfigWidget()
    win.show()
    sys.exit(app.exec_())


