import sys
import math  # +++
import random

from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPointF
from PyQt5 import uic

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = 's'
        uic.loadUi('rbk.ui', self)
        self.pushButton.clicked.connect(self.paint)

    def getRandomSize(self):
        return random.randint(50, 100)

    def getRandomColor(self):
        return QColor(250, 250, 0)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_triangle(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def draw_triangle(self, qp):
        a = self.getRandomSize()
        d = a * math.tan(math.radians(30))
        g = random.randint(0, 450)

        pos_top = QPointF(g, g - d * 2)
        pos_left = QPointF(g - d * 2, g + a)
        pos_right = QPointF(g + d * 2, g + a)

        qp.setBrush(self.getRandomColor())
        path = QPainterPath()
        path.moveTo(pos_top)
        path.lineTo(pos_right)
        path.lineTo(pos_left)

        qp.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())