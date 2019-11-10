import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from UI import Ui_Form


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('Random circles')
        self.draw = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircles(qp)
        qp.end()

    def drawCircles(self, qp):
        if self.draw:
            pen = QPen(self.color, 2)
            qp.setPen(pen)
            qp.drawEllipse(self.x, self.y, self.diam, self.diam)
            self.draw = False

    def run(self):
        self.draw = True
        self.x = randint(0, 590)
        self.y = randint(0, 430)
        self.diam = randint(10, 200)
        self.color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
