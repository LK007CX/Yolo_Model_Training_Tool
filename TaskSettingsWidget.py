#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


"""
1.任务设置页面
"""
class TaskSettingsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(TaskSettingsWidget, self).__init__(*args, **kwargs)
        
        self.listWidget = QListWidget(self)
        
        self.nextStepPushButton = QPushButton("下一步")
        self.nextStepPushButton.setMaximumWidth(100)

        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
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
        newWidget = ItemWidget("image/new.png", "新建训练任务", 0, newItem, self.listWidget)
        self.listWidget.setItemWidget(newItem, newWidget)

        saveItem = QListWidgetItem(self.listWidget)
        saveItem.setSizeHint(QSize(200, 50))
        saveWidget = ItemWidget("image/file.png", "设置保存路径", 1, saveItem, self.listWidget)
        self.listWidget.setItemWidget(saveItem, saveWidget)

        modelCateoryItem = QListWidgetItem(self.listWidget)
        modelCateoryItem.setSizeHint(QSize(200, 50))
        modelCateoryWidget = ModelCateoryWidget("image/category.png", "模型种类选择", modelCateoryItem, self.listWidget)
        self.listWidget.setItemWidget(modelCateoryItem, modelCateoryWidget)

        classNumberItem = QListWidgetItem(self.listWidget)
        classNumberItem.setSizeHint(QSize(200, 50))
        classNumberWidget = ClassNumberWidget("image/number.png", "训练类别数量", classNumberItem, self.listWidget)
        self.listWidget.setItemWidget(classNumberItem, classNumberWidget)





class ItemWidget(QWidget):
    def __init__(self, icon, title, is_open_file, item, *args, **kwargs):
        super(ItemWidget, self).__init__(*args, **kwargs)
        
        self._item = item
        self.icon = icon
        self.title = title
        self.is_open_file = is_open_file

        self.iconLabel = QLabel()
        
        self.titleLabel = QLabel(self.title)
        self.lineEdit = QLineEdit()
        self.operationToolButton = QToolButton()
            
        layout = QHBoxLayout()
        layout.addWidget(self.iconLabel)
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.operationToolButton)
        if not self.is_open_file:
            self.operationToolButton.setVisible(False)
        self.setLayout(layout)
        
        self.initUI()

    
    def initUI(self):
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setPixmap(QPixmap(self.icon))
        self.iconLabel.setMaximumSize(20, 20)
        self.operationToolButton.setText("...")
        self.operationToolButton.setFixedSize(25, 25)

       


class ModelCateoryWidget(QWidget):
    def __init__(self, icon, title, item, *args, **kwargs):
        super(ModelCateoryWidget, self).__init__(*args, **kwargs)

        self._item = item
        self.icon = icon
        self.title = title

        self.iconLabel = QLabel()
        self.titleLabel = QLabel(self.title)
        self.modelCategoryComboBox = QComboBox()
        

        layout = QHBoxLayout()
        layout.addWidget(self.iconLabel)
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.modelCategoryComboBox)
        self.setLayout(layout)
        self.initUI()
    
    def initUI(self):
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setPixmap(QPixmap(self.icon))
        self.iconLabel.setMaximumSize(20, 20)
        self.modelCategoryComboBox.addItem("Yolo V4 Tiny")
        self.modelCategoryComboBox.addItem("Yolo V4")



class ClassNumberWidget(QWidget):
    def __init__(self, icon, title, item, *args, **kwargs):
        super(ClassNumberWidget, self).__init__(*args, **kwargs)

        self._item = item
        self.icon = icon
        self.title = title

        self.iconLabel = QLabel()
        self.titleLabel = QLabel(self.title)
        self.classNumberSlider = QSlider(Qt.Horizontal)
        self.classNumberLabel = QLabel("2")
        

        layout = QHBoxLayout()
        layout.addWidget(self.iconLabel)
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.classNumberSlider)
        layout.addWidget(self.classNumberLabel)
        self.setLayout(layout)
        self.initUI()
    
    def initUI(self):
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setPixmap(QPixmap(self.icon))
        self.iconLabel.setMaximumSize(20, 20)
        self.classNumberSlider.setMinimum(1)
        self.classNumberSlider.setMaximum(80)
        self.classNumberSlider.setSingleStep(1)
        self.classNumberSlider.setValue(2)
        self.classNumberSlider.setTickPosition(QSlider.TicksBelow)
        self.classNumberSlider.valueChanged.connect(self.valueChange)
    
    def valueChange(self, value):
        self.classNumberLabel.setText(str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelCateoryItem = QListWidgetItem()
    win = ModelCateoryWidget("image/file.png", "模型种类选择", modelCateoryItem)
    win = TaskSettingsWidget()
    win.show()
    sys.exit(app.exec_())


