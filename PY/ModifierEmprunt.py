from PYConverted.Modifier_emprunt import Ui_Dialog
from PyQt5.QtWidgets import *

class ModifierEmprunt :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm = isimm
        self.ui.Modifier.clicked.connect(self.Modifier_emprunt)
        self.ui.comboBox_emprunt.currentTextChanged.connect(self.afficher_information)

        for e in self.isimm.empruntes:
            l = self.isimm.recherche_livre(e.reference)
            self.ui.comboBox_emprunt.addItem(str(e.numero_inscription) + " " + str(e.reference) + " " + l.titre)

    def Modifier_emprunt(self):
        ch=self.ui.comboBox_emprunt.currentText().split(" ")
        print(self.isimm.empruntes)
        num = ch[0]
        date_emprunt = self.ui.dateEdit.date()
        date_retour = self.ui.dateEdit_2.date()

        # control de saisie
        if(date_retour<=date_emprunt):
            self.showDialog("ereur", "La date de retour doit être superieur â celle d'emprunt", False)
            return

        self.isimm.modifier_emprunt(num,date_emprunt,date_retour)
        self.showDialog("succès", "Modification terminé", True)



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
    def afficher_information(self):
        num_insc=self.ui.comboBox_emprunt.currentText().split(" ")[0]
        emprunt=self.isimm.recherche_emprunt(num_insc)
        self.ui.dateEdit.setDate(emprunt.date_emprunt)
        self.ui.dateEdit_2.setDate(emprunt.date_retour)
