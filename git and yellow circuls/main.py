import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('UI', self)

        # Находите кнопку в интерфейсе по её имени (предположим, что имя кнопки - pushButton)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        # Создайте окружность
        circle = Circle()

        # Добавьте окружность в виджет вашего интерфейса
        self.verticalLayout.addWidget(circle)



class Circle(QWidget):
    def __init__(self):
        super(Circle, self).__init__()
        diameter = random.randint(20, 100)
        self.setGeometry(0, 0, diameter, diameter)
        self.setStyleSheet("background-color: yellow; border-radius: {}px;".format(diameter / 2))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
