from DB import DBclass
import login_window
import dbeditor
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Auth:
    def login(self, name = None, password = None):
        verify = DBclass()
        if verify.check():
            print(f"Successfully! {name} {password}")

            """print("Open DB Editor")
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = dbeditor.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())"""


