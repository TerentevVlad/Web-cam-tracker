# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 380, 271, 111))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 20, 160, 22))
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 41, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(90, 50, 160, 22))
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(90, 80, 160, 22))
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 470, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройки"))
        self.checkBox.setText(_translate("MainWindow", "H"))
        self.checkBox_2.setText(_translate("MainWindow", "S"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.checkBox_3.setText(_translate("MainWindow", "V"))
        self.pushButton.setText(_translate("MainWindow", "Setting"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))

