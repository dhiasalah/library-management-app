# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Recherche_emprunt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1232, 832)
        Dialog.setStyleSheet("background-color:#0b1dba;\n"
"color:white;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("font: 75 30pt \"Cambria\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(30)
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
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_4.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_4.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_4.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_4.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_4.addWidget(self.radioButton_6)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout_7.addWidget(self.groupBox_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(4)
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(40, 0, 40, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.edit_reference = QtWidgets.QLineEdit(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_reference.setFont(font)
        self.edit_reference.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.edit_reference.setObjectName("edit_reference")
        self.verticalLayout_6.addWidget(self.edit_reference)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.edit_numero_insc = QtWidgets.QLineEdit(self.frame_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_numero_insc.setFont(font)
        self.edit_numero_insc.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.edit_numero_insc.setObjectName("edit_numero_insc")
        self.verticalLayout_5.addWidget(self.edit_numero_insc)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit.setStyleSheet("height:30px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_5.addWidget(self.dateEdit)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(-1, 12, -1, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_2.setStyleSheet("height:30px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_3.setStyleSheet("height:30px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.horizontalLayout_8.addWidget(self.dateEdit_3)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_4.setFont(font)
        self.dateEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_4.setStyleSheet("height:30px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_8.addWidget(self.dateEdit_4)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_5.setFont(font)
        self.dateEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_5.setStyleSheet("height:30px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.horizontalLayout_2.addWidget(self.dateEdit_5)
        self.dateEdit_6 = QtWidgets.QDateEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit_6.setFont(font)
        self.dateEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_6.setStyleSheet("height:30px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.horizontalLayout_2.addWidget(self.dateEdit_6)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(5, 1)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(200, 0, 200, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Rechercher = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Rechercher.setFont(font)
        self.Rechercher.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Rechercher.setStyleSheet("background-color:white;\n"
"color:#0b1dba;\n"
"border-radius:15px;\n"
"height:50;\n"
"font: 75 25pt \"Cambria\";\n"
"")
        self.Rechercher.setObjectName("Rechercher")
        self.horizontalLayout_6.addWidget(self.Rechercher)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableView = QtWidgets.QTableView(self.frame_5)
        self.tableView.setStyleSheet("background:white;\n"
"color:black")
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_4.addWidget(self.tableView)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 6)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Rechercher des emprunts"))
        self.radioButton.setText(_translate("Dialog", "Rechercher un emprunt par livre"))
        self.radioButton_2.setText(_translate("Dialog", "Rechercher un emprunt par étudiant"))
        self.radioButton_3.setText(_translate("Dialog", "Rechercher des livres empruntés â une date donnée"))
        self.radioButton_4.setText(_translate("Dialog", "Rechercher des livres retournés â une date donnée"))
        self.radioButton_5.setText(_translate("Dialog", "Rechercher des livres empruntés entre 2 dates données"))
        self.radioButton_6.setText(_translate("Dialog", "Rechercher des livres retournés entre 2 dates données"))
        self.edit_reference.setPlaceholderText(_translate("Dialog", "Référence d\'un livre"))
        self.edit_numero_insc.setPlaceholderText(_translate("Dialog", "Numero inscription d\'étudiant"))
        self.Rechercher.setText(_translate("Dialog", "Rechercher"))
