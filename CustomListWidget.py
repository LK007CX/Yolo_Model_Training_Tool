#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qdarkstyle
import sys


# 美化样式表
Stylesheet = """
QWidget {
    background-color: rgb(24, 25, 29);
    font-size: 20px;
}
"""


"""
尝试自定义QListWidgetItem
失败
"""
class CustomListWidget(QWidget):

    itemDeleted = pyqtSignal(QListWidgetItem)

    def __init__(self, name, icon, item, *args, **kwargs):
        super(CustomListWidget, self).__init__(*args, **kwargs)
        self.name = name
        self.icon = icon
        self._item = item # 保留list item的对象引用
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(name, self)
        #self.label_title.setScaledContents(True)
        #self.label_title.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label_title.setStyleSheet("""font-size: 20px;font-family: MicroSoft YaHei""")
        self.label_icon = QLabel(self)
        #self.label_icon.setScaledContents(True)
        self.label_icon.setPixmap(QPixmap(self.icon))

        layout.addWidget(self.label_title, 0, Qt.AlignCenter)
        layout.addWidget(self.label_icon, 0, Qt.AlignCenter)

        self.setLayout(layout)
        self.resize(QSize(150, 150))
        #self.setStyleSheet(Stylesheet)

    def doDeleteItem(self):
        self.itemDeleted.emit(self._item)

    def sizeHint(self):
        # 决定item的高度
        return QSize(200, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    item = QListWidgetItem()
    win = CustomListWidget("导入标注", "Data/miaozhun.png", item)
    win.show()
    sys.exit(app.exec_())