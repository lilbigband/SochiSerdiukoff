import sys
import math  # +++
import random

from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPointF
from rbk import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = 's'
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_triangle(qp)
        qp.end()

    def paint(self):
        self.repaint()

    def draw_triangle(self, qp):
        d = random.randint(50, 300)
        self.colour_r = random.randint(0, 255)
        self.colour_g = random.randint(0, 255)
        self.colour_b = random.randint(0, 255)
        qp.setBrush(QColor(self.colour_r, self.colour_g, self.colour_b))
        qp.drawEllipse(random.randint(50, 400), random.randint(50, 250), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())