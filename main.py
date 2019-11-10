import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.draw = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp):
        if self.draw:
            pen = QPen(QColor(255, 255, 0), 2)
            qp.setPen(pen)
            qp.drawEllipse(self.x, self.y, self.diam, self.diam)
            self.draw = False

    def run(self):
        self.draw = True
        self.x = randint(0, 590)
        self.y = randint(0, 430)
        self.diam = randint(10, 200)
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
