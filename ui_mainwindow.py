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
        MainWindow.resize(263, 368)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_Particulas = QGroupBox(self.centralwidget)
        self.groupBox_Particulas.setObjectName(u"groupBox_Particulas")
        self.gridLayout = QGridLayout(self.groupBox_Particulas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_id = QLabel(self.groupBox_Particulas)
        self.label_id.setObjectName(u"label_id")

        self.gridLayout.addWidget(self.label_id, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_Particulas)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_origenX = QLabel(self.groupBox_Particulas)
        self.label_origenX.setObjectName(u"label_origenX")

        self.gridLayout.addWidget(self.label_origenX, 1, 0, 1, 1)

        self.spinBox = QSpinBox(self.groupBox_Particulas)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)

        self.label_origenY = QLabel(self.groupBox_Particulas)
        self.label_origenY.setObjectName(u"label_origenY")

        self.gridLayout.addWidget(self.label_origenY, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_2, 2, 1, 1, 1)

        self.label_destinoX = QLabel(self.groupBox_Particulas)
        self.label_destinoX.setObjectName(u"label_destinoX")

        self.gridLayout.addWidget(self.label_destinoX, 3, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_3, 3, 1, 1, 1)

        self.label_destinoY = QLabel(self.groupBox_Particulas)
        self.label_destinoY.setObjectName(u"label_destinoY")

        self.gridLayout.addWidget(self.label_destinoY, 4, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(500)

        self.gridLayout.addWidget(self.spinBox_4, 4, 1, 1, 1)

        self.label_velocidad = QLabel(self.groupBox_Particulas)
        self.label_velocidad.setObjectName(u"label_velocidad")

        self.gridLayout.addWidget(self.label_velocidad, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_Particulas)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 1)

        self.label_color = QLabel(self.groupBox_Particulas)
        self.label_color.setObjectName(u"label_color")

        self.gridLayout.addWidget(self.label_color, 6, 0, 1, 1)

        self.label_red = QLabel(self.groupBox_Particulas)
        self.label_red.setObjectName(u"label_red")

        self.gridLayout.addWidget(self.label_red, 7, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_5, 7, 1, 1, 1)

        self.label_green = QLabel(self.groupBox_Particulas)
        self.label_green.setObjectName(u"label_green")

        self.gridLayout.addWidget(self.label_green, 8, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_6, 8, 1, 1, 1)

        self.label_blue = QLabel(self.groupBox_Particulas)
        self.label_blue.setObjectName(u"label_blue")

        self.gridLayout.addWidget(self.label_blue, 9, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox_Particulas)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setMaximum(255)
        self.spinBox_7.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.gridLayout.addWidget(self.spinBox_7, 9, 1, 1, 1)

        self.pushButton_Agregar = QPushButton(self.groupBox_Particulas)
        self.pushButton_Agregar.setObjectName(u"pushButton_Agregar")

        self.gridLayout.addWidget(self.pushButton_Agregar, 10, 0, 1, 2)


        self.gridLayout_2.addWidget(self.groupBox_Particulas, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 263, 21))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Algoritmia", None))
        self.groupBox_Particulas.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"iD:", None))
        self.label_origenX.setText(QCoreApplication.translate("MainWindow", u"Origen(x):", None))
        self.label_origenY.setText(QCoreApplication.translate("MainWindow", u"Origen(Y)", None))
        self.label_destinoX.setText(QCoreApplication.translate("MainWindow", u"Destino(X)", None))
        self.label_destinoY.setText(QCoreApplication.translate("MainWindow", u"Destino(Y)", None))
        self.label_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"red:", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"green:", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"blue:", None))
        self.pushButton_Agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

