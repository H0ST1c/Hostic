# он правда генерирует жёлтые окружности, просто их не видно, потому что они жёлтые
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)
        self.window().setFixedSize(500, 500)
        self.pushButton.clicked.connect(self.generate_circle)
        self.circle_diameters = []

    def generate_circle(self):
        diameter = random.randint(10, 100)
        self.circle_diameters.append(diameter)
        self.update_circle_container()

    def update_circle_container(self):
        for i in range(self.gridLayout.count()):
            item = self.gridLayout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()

        for diameter in self.circle_diameters:
            circle_widget = CircleWidget(diameter)
            self.gridLayout.addWidget(circle_widget, random.randint(0, 500), random.randint(0, 500))


class CircleWidget(QWidget):
    def __init__(self, diameter):
        super(CircleWidget, self).__init__()
        self.diameter = diameter
        self.setMinimumSize(diameter, diameter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor("yellow"))
        painter.drawEllipse(0, 0, self.diameter, self.diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
