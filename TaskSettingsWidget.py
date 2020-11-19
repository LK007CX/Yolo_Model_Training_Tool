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

        classAddItem = QListWidgetItem(self.listWidget)
        classAddItem.setSizeHint(QSize(200, 300))
        classAddWidget = ClassAddWidget("image/label.png", "添加训练标签", classAddItem, self.listWidget)
        self.listWidget.setItemWidget(classAddItem, classAddWidget)


'''
训练任务设置
'''
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

       

'''
模型种类选择
'''
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



'''
训练类别数量
'''
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


'''
训练类别添加
'''
class ClassAddWidget(QWidget):
    def __init__(self, icon, title, item, *args, **kwargs):
        super(ClassAddWidget, self).__init__(*args, **kwargs)

        self._item = item
        self.icon = icon
        self.title = title

        self.iconLabel = QLabel()
        self.titleLabel = QLabel(self.title)
        self.classAddLineEdit = QLineEdit()
        self.classAddPushButton = QPushButton("添加类别")
        self.classAllDeletePushButton = QPushButton("删除全部类别")
        self.classListWidget = QListWidget()
        
        hBoxlayout = QHBoxLayout()
        hBoxlayout.addWidget(self.iconLabel)
        hBoxlayout.addWidget(self.titleLabel)
        hBoxlayout.addWidget(self.classAddLineEdit)
        hBoxlayout.addWidget(self.classAddPushButton)
        hBoxlayout.addWidget(self.classAllDeletePushButton)
        vBoxlayout = QVBoxLayout()
        vBoxlayout.addLayout(hBoxlayout)
        vBoxlayout.addWidget(self.classListWidget)
        self.setLayout(vBoxlayout)
        self.initUI()

        
    
    def initUI(self):
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setPixmap(QPixmap(self.icon))
        self.iconLabel.setMaximumSize(20, 20)
        self.classAddPushButton.clicked.connect(self.addClassItem)
        self.classAllDeletePushButton.clicked.connect(self.doClearItem)

    
    def addClassItem(self):
        text = str(self.classAddLineEdit.text()).strip()
        if text == '':
            return
        self.classAddLineEdit.clear()
        item = QListWidgetItem(self.classListWidget)
        item.setSizeHint(QSize(200, 30))
        widget = ClassItemWidget(text, item, self.classListWidget)
        widget.itemDeleted.connect(self.doDeleteItem)
        self.classListWidget.setItemWidget(item, widget)

    
    def doClearItem(self):
        # 清空所有Item
        for _ in range(self.classListWidget.count()):
            # 删除item
            # 一直是0的原因是一直从第一行删,删掉第一行后第二行变成了第一行
            # 这个和删除list [] 里的数据是一个道理
            item = self.classListWidget.takeItem(0)
            # 删除widget
            self.classListWidget.removeItemWidget(item)
            del item

    def doDeleteItem(self, item):
        # 根据item得到它对应的行数
        row = self.classListWidget.indexFromItem(item).row()
        # 删除item
        item = self.classListWidget.takeItem(row)
        # 删除widget
        self.classListWidget.removeItemWidget(item)
        del item
    
    def check():
        # 检查是否有重复项，是否有中文标签
        pass

class ClassItemWidget(QWidget):

    itemDeleted = pyqtSignal(QListWidgetItem)

    def __init__(self, text, item, *args, **kwargs):
        super(ClassItemWidget, self).__init__(*args, **kwargs)
        self._item = item  # 保留list item的对象引用

        self.classNameLabel = QLabel(text)
        self.deletePushButton = QPushButton('删除', clicked=self.doDeleteItem)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.classNameLabel)
        layout.addWidget(self.deletePushButton)
        self.initUI()

    def initUI(self):
        self.deletePushButton.setMaximumWidth(100)

    def doDeleteItem(self):
        self.itemDeleted.emit(self._item)

    def sizeHint(self):
        # 决定item的高度
        return QSize(200, 40)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    modelCateoryItem = QListWidgetItem()
    win = ModelCateoryWidget("image/file.png", "模型种类选择", modelCateoryItem)
    win = TaskSettingsWidget()
    win.resize(800, 800)
    win.show()
    sys.exit(app.exec_())


