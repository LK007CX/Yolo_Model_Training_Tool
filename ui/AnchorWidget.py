#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


"""
4.
"""


class AnchorWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(AnchorWidget, self).__init__(*args, **kwargs)
        
        self.label = QLabel("Anchor", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AnchorWidget()
    win.show()
    sys.exit(app.exec_())


