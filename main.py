from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from dbeditor import Ui_DBEditor
from login_window import Ui_MainWindow
from DB import DBclass

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def openDBeditor():
    check = DBclass()
    login = ui.login_line.text()
    password = ui.password_line.text()


    if check.check(login, password):
        global DBEditro

        DBEditro = QtWidgets.QMainWindow()
        uibd = Ui_DBEditor()
        uibd.setupUi(DBEditro)
        MainWindow.close()
        print("Login window close")
        DBEditro.show()
        print("Open DBEditor")


ui.login_button.clicked.connect(openDBeditor)

sys.exit(app.exec())

