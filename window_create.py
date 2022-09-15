import login_window
import dbeditor
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Window_auth:
    def init_window(self):
        print("Open auth window")
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = login_window.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())



class Window_DbEditor():
    def init_window(self):
        print("Open DB Editor")
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = dbeditor.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
