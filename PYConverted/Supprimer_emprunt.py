# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Supprimer_emprunt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1170, 788)
        Dialog.setStyleSheet("background-color:#0b1dba;\n"
"color:white;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("font: 75 40pt \"Cambria\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setContentsMargins(10, 6, 181, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 20pt \"Cambria\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_emprunt = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_emprunt.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_emprunt.setFont(font)
        self.comboBox_emprunt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_emprunt.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.comboBox_emprunt.setObjectName("comboBox_emprunt")
        self.horizontalLayout_2.addWidget(self.comboBox_emprunt)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_7.addWidget(self.groupBox_4)
        self.horizontalLayout_7.setStretch(0, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(200, -1, 200, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Supprimer = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Supprimer.setFont(font)
        self.Supprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Supprimer.setStyleSheet("background-color:white;\n"
"color:#0b1dba;\n"
"border-radius:15px;\n"
"height:51;\n"
"font: 75 25pt \"Cambria\";\n"
"")
        self.Supprimer.setObjectName("Supprimer")
        self.horizontalLayout_6.addWidget(self.Supprimer)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Suppression des Emprunts"))
        self.label_2.setText(_translate("Dialog", "Supprimer un emprunt"))
        self.Supprimer.setText(_translate("Dialog", "Supprimer"))