import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.lelow)


    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.r = randint(10, 100)
            self.x = randint(10, 200)
            self.y = randint(10, 200)
            self.qp.setPen(QColor(255, 255, 0))
            self.draw(self.r, self.x, self.y)
            self.qp.end()

    def draw(self, r, x, y):
            self.qp.drawEllipse(x, y, r, r)


    def lelow(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())