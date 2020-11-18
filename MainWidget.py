#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qdarkstyle
from CustomListWidget import CustomListWidget
from TaskSettingsWidget import TaskSettingsWidget
import sys




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

        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        
        self.setWindowTitle("模型训练工具")
        self.setWindowIcon(QIcon("Data/darknet.png"))

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
        
        item_start = QListWidgetItem(
                QIcon('Data/home.png'), "1.任务设置", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_start.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_start.setTextAlignment(Qt.AlignCenter)

        item_tagging = QListWidgetItem(
                QIcon('Data/tagging.png'), "2.导入标注", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_tagging.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_tagging.setTextAlignment(Qt.AlignCenter)

        item_cfg = QListWidgetItem(
                QIcon('Data/setting.png'), "3.修改配置", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_cfg.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_cfg.setTextAlignment(Qt.AlignCenter)


        item_train = QListWidgetItem(
                QIcon('Data/train.png'), "4.开始训练", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_train.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_train.setTextAlignment(Qt.AlignCenter)


        item_test = QListWidgetItem(
                QIcon('Data/test.png'), "5.测试模型", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_test.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_test.setTextAlignment(Qt.AlignCenter)

        item_map = QListWidgetItem(
                QIcon('Data/性能统计.png'), "6.性能统计", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_map.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_map.setTextAlignment(Qt.AlignCenter)

        item_anchor = QListWidgetItem(
                QIcon('Data/anchor.png'), "7.聚类分析", self.listWidget)
        # 设置item的默认宽高(这里只有高度比较有用)
        item_anchor.setSizeHint(QSize(16777215, 100))
        # 文字居中
        item_anchor.setTextAlignment(Qt.AlignCenter)

        taskSettingsWidget = TaskSettingsWidget()
        taskSettingsWidget.setContentsMargins(300, 200, 300, 350)
        #taskSettingsWidget.setStyleSheet("""margin: 50px;""")
        self.stackedWidget.addWidget(taskSettingsWidget)

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())