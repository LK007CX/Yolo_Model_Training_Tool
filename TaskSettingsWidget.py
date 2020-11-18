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
/*去掉item虚线边框*/
QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}
/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/
QListWidget {
    color: black;
    background: white;
    font-size: 20px;
}

"""


class TaskSettingsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TaskSettingsWidget, self).__init__(*args, **kwargs)
        
        self.listWidget = QListWidget(self)
        self.nextStepPushButton = QPushButton("下一步")
        self.nextStepPushButton.setMaximumWidth(100)
        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
        #layout.addWidget(self.nextStepPushButton)

        # layout.addWidget(self.listWidget, 0, Qt.AlignCenter)
        layout.addWidget(self.nextStepPushButton, 0, Qt.AlignCenter)

        self.setLayout(layout)
        
       
        self.initUI()
    
    def initUI(self):
        # 去掉边框
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # self.nextStepPushButton.setMaximumWidth(200)
        newItem = QListWidgetItem(self.listWidget)
        newItem.setSizeHint(QSize(200, 50))
        newWidget = ItemWidget("Data/new.png", "新建训练任务", 0, newItem, self.listWidget)
        self.listWidget.setItemWidget(newItem, newWidget)

        saveItem = QListWidgetItem(self.listWidget)
        saveItem.setSizeHint(QSize(200, 50))
        saveWidget = ItemWidget("Data/file.png", "设置保存路径", 1, saveItem, self.listWidget)
        self.listWidget.setItemWidget(saveItem, saveWidget)

class ItemWidget(QWidget):
    def __init__(self, icon, title, is_open_file, item, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        
        self._item = item
        self.icon = icon
        self.title = title
        self.is_open_file = is_open_file

        self.iconLabel = QLabel()
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setPixmap(QPixmap(self.icon))
        self.iconLabel.setMaximumSize(20, 20)
        self.titleLabel = QLabel(self.title)
        self.lineEdit = QLineEdit()
        self.operationToolButton = QToolButton()
        self.operationToolButton.setText("...")
        self.operationToolButton.setFixedSize(25, 25)        
        layout = QHBoxLayout()
        layout.addWidget(self.iconLabel)
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.operationToolButton)
        if not self.is_open_file:
            self.operationToolButton.setVisible(False)
        self.setLayout(layout)
        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TaskSettingsWidget()
    win.show()
    sys.exit(app.exec_())


