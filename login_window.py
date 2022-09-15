# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from login import Auth
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 200)
        MainWindow.setMinimumSize(QtCore.QSize(300, 200))
        MainWindow.setMaximumSize(QtCore.QSize(300, 200))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, 50, 30, 50)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line.setText("")
        self.login_line.setObjectName("login_line")
        self.verticalLayout.addWidget(self.login_line)
        self.password_line = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line.setText("")
        self.password_line.setObjectName("password_line")
        self.verticalLayout.addWidget(self.password_line)
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setObjectName("login_button")
        self.verticalLayout.addWidget(self.login_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.give_logpass()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AximeTableEditor   Login"))
        self.login_line.setPlaceholderText(_translate("MainWindow", "Login"))
        self.password_line.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))

    def give_logpass(self):
        self.login_button.clicked.connect(self.click)

    def click(self):
        login = self.login_line.text()
        password = self.password_line.text()
        auth = Auth()
        auth.login(login,password)