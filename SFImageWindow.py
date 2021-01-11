from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *


class SFImageWindow(QtWidgets.QLabel):
    is_editPolygon = True
    is_createPolygon = False
    polygonList = []
    pos = None

    def __init__(self, parent=None):
        super(SFImageWindow, self).__init__(parent)

    # 重写鼠标点击事件
    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        if self.is_createPolygon:
            # 如果点击时数组不为空，点击后直接画线
            if not self.polygonList:
                self.pos = ev.windowPos()
                self.update()
            # 不管是否为空都加入数组
            self.polygonList.append(ev.windowPos())

    # 重写鼠标移动事件
    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        self.pos = event.windowPos()
        self.setMouseTracking(True)
        if self.is_createPolygon:
            if self.polygonList:
                pass
            else:
                self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        previous_point = self.polygonList[-1]
        q = QPainter(self)
        q.drawLine(previous_point.x(), previous_point.y(), self.pos.x(), self.pos.y())
        self.polygonList.append(self.pos)
