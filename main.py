import maincommandslist
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Axime")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.text = QtWidgets.QLabel(self)
        self.text.setText("Лол кек")
        self.text.move(100, 100)
        self.text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application ():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()













"""
programm_work = True
while programm_work:
    maincommandslist.input_command()
"""
