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
        
        self.label = QLabel("Tagging", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TaggingWidget()
    win.show()
    sys.exit(app.exec_())


