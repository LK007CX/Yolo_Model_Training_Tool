#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import randint

import qdarkstyle
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from CustomListWidget import CustomListWidget
from TaskSettingsWidget import TaskSettingsWidget


"""
主页面
"""
class Winform(QWidget):
    def __init__(self, *args, **kwargs):
        super(Winform, self).__init__(*args, **kwargs)

        self.resize(1280, 720)
        
        # 左侧列表
        self.listWidget = QListWidget(self, objectName="listWidget")

        # 右侧层叠窗口
        self.stackedWidget = QStackedWidget(self)

        # 左右布局(左边一个QListWidget + 右边QStackedWidget)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.listWidget)
        layout.addWidget(self.stackedWidget)
        
        self.initUi()
        
        self.setWindowTitle("模型训练工具")
        self.setWindowIcon(QIcon("image/darknet.png"))

    def initUi(self):
        self.listWidget.setFixedWidth(180)
        self.listWidget.setStyleSheet("""QListWidget {
                                        min-width: 180px;
                                        max-width: 180px;
                                        outline: 0px;
                                        font-size: 15px;
                                        border-right: 10px;
                                        }
                                        /*被选中时的背景颜色和左边框颜色*/
                                        QListWidget::item:selected {
                                        background-color: SkyBlue;
                                        color: black;
                                        border-left: 2px solid rgb(9, 187, 7);
                                        }
                                        
                                        """)
        self.stackedWidget.setStyleSheet("""QStackedWidget {
                                        background-color: white;
                                        border-left: 2px solid rgb(0, 0, 0);
                                        }""")
        # 初始化界面
        self.listWidget.setIconSize(QSize(50, 50))
        # 通过QListWidget的当前item变化来切换QStackedWidget中的序号
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)
        # 去掉边框
        self.listWidget.setFrameShape(QListWidget.NoFrame)
        # 隐藏滚动条
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        

        # 1.任务设置
        startItem = QListWidgetItem(
                QIcon('image/home.png'), "1.任务设置", self.listWidget)
        startItem.setSizeHint(QSize(16777215, 100))
        startItem.setTextAlignment(Qt.AlignCenter)
        
        # 2.导入标注
        taggingItem = QListWidgetItem(
                QIcon('image/tagging.png'), "2.导入标注", self.listWidget)
        taggingItem.setSizeHint(QSize(16777215, 100))
        taggingItem.setTextAlignment(Qt.AlignCenter)
        
        # 3.修改配置
        configItem = QListWidgetItem(
                QIcon('image/setting.png'), "3.修改配置", self.listWidget)
        configItem.setSizeHint(QSize(16777215, 100))
        configItem.setTextAlignment(Qt.AlignCenter)

        # 4.开始训练
        trainItem = QListWidgetItem(
                QIcon('image/train.png'), "4.开始训练", self.listWidget)
        trainItem.setSizeHint(QSize(16777215, 100))
        trainItem.setTextAlignment(Qt.AlignCenter)

        # 5.测试模型
        testItem = QListWidgetItem(
                QIcon('image/test.png'), "5.测试模型", self.listWidget)
        testItem.setSizeHint(QSize(16777215, 100))
        testItem.setTextAlignment(Qt.AlignCenter)
        
        # 6.性能统计
        mapItem = QListWidgetItem(
                QIcon('image/性能统计.png'), "6.性能统计", self.listWidget)
        mapItem.setSizeHint(QSize(16777215, 100))
        mapItem.setTextAlignment(Qt.AlignCenter)
        
        # 7.聚类分析
        anchorItem = QListWidgetItem(
                QIcon('image/anchor.png'), "7.聚类分析", self.listWidget)
        anchorItem.setSizeHint(QSize(16777215, 100))
        anchorItem.setTextAlignment(Qt.AlignCenter)

        taskSettingsWidget = TaskSettingsWidget()
        taskSettingsWidget.setContentsMargins(200, 200, 200, 200)
        self.stackedWidget.addWidget(taskSettingsWidget)

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())
