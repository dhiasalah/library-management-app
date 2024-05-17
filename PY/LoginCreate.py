import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
import os
from playsound import playsound
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PY.Account import Account
from PY.ISIMM import ISIMM
from PY.MainWindow import MainWindow
from PYConverted.create_acc import  Ui_Dialog as create
from PYConverted.login import  Ui_Dialog as login


class Login:
    def __init__(self,isimm):
        self.isimm = isimm
        self.window = QDialog()
        self.ui = login()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.loginbutton.clicked.connect(self.loginfunction)

        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.createaccbutton.clicked.connect(self.gotocreate)
        self.isconnected=False
        self.recupererAccount()

    def loginfunction(self):
        email=self.ui.email.text()
        password=self.ui.password.text()
        if (email == "" or len(email) < 5):
            self.showDialog("ereur", "Username doit contenir au moins 5 caractères", False)
            return
        if (password == "" or len(password) < 8):
            self.showDialog("ereur", "le mot de passe doit contenir 8 caractères", False)
            return
        if(self.isimm.rechercher_account_paradresse(email) and not self.isimm.rechercher_account_parmotpasse(password)):
            self.showDialog("ereur", "Mot de passe incorrect", False)
            return
        if (self.isimm.recherche_account(email,password)):
            self.isconnected=True
        if(self.isconnected):
            self.window.close()
            self.window2 = MainWindow()

        else:
            self.showDialog("ereur", "compte inexisstant", False)
            return

    def gotocreate(self):
        self.window.close()
        self.createacc=CreateAcc()

    def showDialog(self, title, str, bool):
        msgBox = QMessageBox()
        if bool == False:
            msgBox.setIcon(QMessageBox.Warning)
        else:
            msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    def enregistrerAccount(self):
        F = open("CSV/Accounts.csv", "w+")
        F.seek(0)
        F.write("email,mot_de_passe\n")
        for i in self.isimm.accounts:
            found = False
            for j in F:
                numI = j.split(",")[0]
                if (numI == i.adresse):
                    found = True
                    break
            if (not found):
                F.write(i.adresse + "," + i.mot_passe + "\n")

        F.close()

    def recupererAccount(self):
        self.isimm.accounts.clear()
        F = open("CSV/Accounts.csv", "r")
        count = -1
        for line in F:
            count += 1
            if (count == 0):
                continue
            self.isimm.accounts.append(self.parseStudent(line))

        F.close()

    def parseStudent(self, line):
        lis = line.split(",")
        lis[1] = lis[1].replace("\n", "")
        return Account(lis[0], lis[1])

class CreateAcc:
    def __init__(self):
        self.isimm = ISIMM()
        self.login = Login(self.isimm)
        self.window = QDialog()
        self.ui = create()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.signupbutton.clicked.connect(self.createaccfunction)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.ui.email.text()
        password = self.ui.password.text()
        if ( email=="" or len(email)<5):
            self.showDialog("ereur", "Username invalide", False)
            return
        if(password=="" or len(password)<8):
            self.showDialog("ereur", "le mot de passe doit contenir 8 caractères", False)
            return
        if self.ui.password.text()!=self.ui.confirmpass.text():
            self.showDialog("ereur", "vérifier la confirmation de votre mot de passe", False)
            return
        if (self.isimm.rechercher_account_paradresse(email)):
            self.showDialog("ereur", "non d'utilisateur exisste déja", False)
            return
        print(self.isimm.accounts)
        new_account = Account(email,password)
        self.isimm.ajouter_account(new_account)
        print(self.isimm.accounts)
        self.showDialog("succès", "compte ajouté", True)
        self.login.enregistrerAccount()
        print("Successfully created acc with email: ", email, "and password: ", password)
        self.login = Login(self.isimm)
        self.window.close()



    def showDialog(self, title, str, bool):
        msgBox = QMessageBox()
        if bool == False:
            msgBox.setIcon(QMessageBox.Warning)
        else:
            msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(str)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
