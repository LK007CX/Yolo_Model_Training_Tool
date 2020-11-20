#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
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

        self.imagePath = None
        self.xmlPath = None

        self.prevPushButton = QPushButton()
        self.nextPushButton = QPushButton()

        self.imageChooseWidget = FileChooseWidget('image/file.png', "图片位置选择")
        self.xmlChooseWidget = FileChooseWidget('image/file.png', "标注位置选择")


        self.imageListWidget = QListWidget()
        self.xmlListWidget = QListWidget()

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
        rightLayout.addWidget(self.imageChooseWidget)
        rightLayout.addWidget(self.xmlChooseWidget)
        rightLayout.addWidget(self.imageListWidget)
        rightLayout.addWidget(self.xmlListWidget)
        rightLayout.addStretch(10)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)

        self.setLayout(layout)

    def resizeEvent(self, QResizeEvent):
        base = self.width() // 25
        self.imageLabel.setFixedSize(QSize(16 * base, 9 * base))
    
    def initUI(self):
        base = self.width() // 25
        self.imageLabel.setFixedSize(QSize(16*base, 9*base))
        self.imageLabel.setStyleSheet("""QLabel {background-color: rgb(45, 45, 45)}""")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setMinimumSize(QSize(640, 320))
        self.prevPushButton.setIcon(QIcon('image/prev.png'))
        self.prevPushButton.setMinimumSize(QSize(100, 50))
        self.prevPushButton.setIconSize(QSize(45, 45))
        self.nextPushButton.setIcon(QIcon('image/next.png'))
        self.nextPushButton.setMinimumSize(QSize(100, 50))
        self.nextPushButton.setIconSize(QSize(45, 45))
        self.imageListWidget.setMaximumWidth(300)
        self.xmlListWidget.setMaximumWidth(300)

        self.imageListWidget.currentRowChanged.connect(self.xmlListWidget.setCurrentRow)
        self.xmlListWidget.currentRowChanged.connect(self.imageListWidget.setCurrentRow)


        self.imageChooseWidget.operationPushButton.clicked.connect(self.chooseImagePath)
        self.xmlChooseWidget.operationPushButton.clicked.connect(self.chooseXMLPath)

        self.imageChooseWidget.resetPushButton.clicked.connect(self.resetImagePath)
        self.xmlChooseWidget.resetPushButton.clicked.connect(self.resetXMLPath)



    def addImageToListWidget_test(self):
        for i in range(50):
            item = QListWidgetItem(QIcon('image/image.png'), str(' 图 片 %s' % i), self.imageListWidget)

    def addXMLToListWidget_test(self):
        for i in range(50):
            item = QListWidgetItem(QIcon('image/xml_logo.png'), str(' 标 注 %s' % i), self.xmlListWidget)

    def addImageToListWidget(self):
        if self.imagePath == None:
            return
        for file in sorted(os.listdir(self.imagePath)):
            if file.endswith('.jpg'):
                item = QListWidgetItem(QIcon('image/image.png'), file, self.imageListWidget)

    def addXMLToListWidget(self):
        if self.xmlPath == None:
            return
        for file in sorted(os.listdir(self.xmlPath)):
            if file.endswith('.xml'):
                item = QListWidgetItem(QIcon('image/xml_logo.png'), file, self.xmlListWidget)

    def chooseImagePath(self):
        directory = QFileDialog.getExistingDirectory(None, "选取图片存放文件夹", "./")
        if directory == '':
            return
        self.imageChooseWidget.lineEdit.setText(directory)
        self.imagePath = directory
        self.doClearImageItem(self.imageListWidget)
        self.addImageToListWidget()

    def chooseXMLPath(self):
        directory = QFileDialog.getExistingDirectory(None, "选取标注存放文件夹", "./")
        if directory == '':
            return
        self.xmlChooseWidget.lineEdit.setText(directory)
        self.xmlPath = directory
        self.doClearImageItem(self.xmlListWidget)
        self.addXMLToListWidget()

    def doClearImageItem(self, listWidget):
        # 清空所有Item
        for _ in range(listWidget.count()):
            # 删除item
            # 一直是0的原因是一直从第一行删,删掉第一行后第二行变成了第一行
            # 这个和删除list [] 里的数据是一个道理
            item = listWidget.takeItem(0)
            # 删除widget
            listWidget.removeItemWidget(item)
            del item

    def resetImagePath(self):
        self.imageChooseWidget.lineEdit.setText('')
        self.imagePath = None

    def resetXMLPath(self):
        self.xmlChooseWidget.lineEdit.setText('')
        self.xmlPath = None


class FileChooseWidget(QWidget):
    def __init__(self, icon, title, *args, **kwargs):
        super(FileChooseWidget, self).__init__(*args, **kwargs)
        
        self.icon = icon
        self.title = title

        self.iconLabel = QLabel()
        self.titleLabel = QLabel(self.title)
        self.lineEdit = QLineEdit()
        self.operationPushButton = QPushButton("打开目录")
        self.resetPushButton = QPushButton("重置")
            
        layout = QFormLayout()
        layout.addRow(self.iconLabel, self.titleLabel)
        layout.addRow(self.lineEdit)
        layout.addRow(self.operationPushButton, self.resetPushButton)
        self.setLayout(layout)
        self.setMaximumWidth(300)
        self.initUI()
    
    def initUI(self):
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setPixmap(QPixmap(self.icon))
        self.iconLabel.setMaximumSize(20, 20)
        self.lineEdit.setReadOnly(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TaggingWidget()
    win.show()
    sys.exit(app.exec_())


