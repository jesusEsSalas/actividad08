# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_Particulas = QGroupBox(self.centralwidget)
        self.groupBox_Particulas.setObjectName(u"groupBox_Particulas")
        self.groupBox_Particulas.setGeometry(QRect(290, 80, 243, 332))
        self.spinBox_7 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(110, 290, 42, 22))
        self.spinBox_7.setMaximum(500)
        self.label_id = QLabel(self.groupBox_Particulas)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setGeometry(QRect(20, 20, 55, 16))
        self.spinBox_5 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(110, 230, 42, 22))
        self.spinBox_5.setMaximum(500)
        self.label_green = QLabel(self.groupBox_Particulas)
        self.label_green.setObjectName(u"label_green")
        self.label_green.setGeometry(QRect(50, 260, 55, 16))
        self.label_color = QLabel(self.groupBox_Particulas)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setGeometry(QRect(20, 200, 55, 16))
        self.lineEdit = QLineEdit(self.groupBox_Particulas)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 20, 113, 22))
        self.spinBox_4 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(110, 140, 42, 22))
        self.spinBox_4.setMaximum(500)
        self.spinBox_6 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(110, 260, 42, 22))
        self.spinBox_6.setMaximum(500)
        self.label_velocidad = QLabel(self.groupBox_Particulas)
        self.label_velocidad.setObjectName(u"label_velocidad")
        self.label_velocidad.setGeometry(QRect(20, 170, 55, 16))
        self.spinBox = QSpinBox(self.groupBox_Particulas)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(110, 50, 42, 22))
        self.spinBox.setMaximum(500)
        self.label_origenX = QLabel(self.groupBox_Particulas)
        self.label_origenX.setObjectName(u"label_origenX")
        self.label_origenX.setGeometry(QRect(20, 50, 55, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox_Particulas)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 170, 113, 22))
        self.label_destinoX = QLabel(self.groupBox_Particulas)
        self.label_destinoX.setObjectName(u"label_destinoX")
        self.label_destinoX.setGeometry(QRect(20, 110, 61, 16))
        self.spinBox_3 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(110, 110, 42, 22))
        self.spinBox_3.setMaximum(500)
        self.label_destinoY = QLabel(self.groupBox_Particulas)
        self.label_destinoY.setObjectName(u"label_destinoY")
        self.label_destinoY.setGeometry(QRect(20, 140, 61, 16))
        self.label_blue = QLabel(self.groupBox_Particulas)
        self.label_blue.setObjectName(u"label_blue")
        self.label_blue.setGeometry(QRect(50, 290, 55, 16))
        self.spinBox_2 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(110, 80, 42, 22))
        self.spinBox_2.setMaximum(500)
        self.label_red = QLabel(self.groupBox_Particulas)
        self.label_red.setObjectName(u"label_red")
        self.label_red.setGeometry(QRect(50, 230, 55, 16))
        self.label_origenY = QLabel(self.groupBox_Particulas)
        self.label_origenY.setObjectName(u"label_origenY")
        self.label_origenY.setGeometry(QRect(20, 80, 55, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 832, 26))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algoritmia", None))
        self.groupBox_Particulas.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"iD:", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"green:", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen(x):", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino(X)", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino(Y)", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"blue:", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"red:", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen(Y)", None))
    # retranslateUi

