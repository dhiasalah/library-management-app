# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Recherche_livre.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1190, 848)
        Dialog.setStyleSheet("background-color:#0b1dba;\n"
"color:white;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
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
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(-1, 24, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_reference = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_reference.setFont(font)
        self.edit_reference.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.edit_reference.setObjectName("edit_reference")
        self.horizontalLayout_3.addWidget(self.edit_reference)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.edit_titre = QtWidgets.QLineEdit(self.frame_10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_titre.setFont(font)
        self.edit_titre.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.edit_titre.setObjectName("edit_titre")
        self.horizontalLayout_8.addWidget(self.edit_titre)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_annee = QtWidgets.QLineEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_annee.setFont(font)
        self.edit_annee.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.edit_annee.setObjectName("edit_annee")
        self.horizontalLayout_2.addWidget(self.edit_annee)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 26)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.edit_auteur = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.edit_auteur.setFont(font)
        self.edit_auteur.setStyleSheet("height:35px;\n"
"border-radius:10px;\n"
"padding-left:25px;\n"
"background-color:white;\n"
"color:black;")
        self.edit_auteur.setObjectName("edit_auteur")
        self.verticalLayout_5.addWidget(self.edit_auteur)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.horizontalLayout_7.addWidget(self.frame_3)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setContentsMargins(200, 0, 200, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Rechercher = QtWidgets.QPushButton(self.frame_12)
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
        self.verticalLayout_2.addWidget(self.frame_12)
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
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Rechercher des livres"))
        self.radioButton.setText(_translate("Dialog", "Rechercher par référence"))
        self.radioButton_2.setText(_translate("Dialog", "Rechercher par titre"))
        self.radioButton_3.setText(_translate("Dialog", "Rechercher par année edition donnée"))
        self.radioButton_4.setText(_translate("Dialog", "Rechercher les livres d\'un auteur donné"))
        self.edit_reference.setPlaceholderText(_translate("Dialog", "Réference"))
        self.edit_titre.setPlaceholderText(_translate("Dialog", "Titre"))
        self.edit_annee.setPlaceholderText(_translate("Dialog", "année édition"))
        self.edit_auteur.setPlaceholderText(_translate("Dialog", "Auteur"))
        self.Rechercher.setText(_translate("Dialog", "Rechercher"))
