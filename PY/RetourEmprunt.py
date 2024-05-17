from PYConverted.Retour_emprunt import Ui_Dialog
from PyQt5.QtWidgets import *

class RetourEmprunt :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm = isimm
        self.ui.Retourner.clicked.connect(self.Retourner_emprunt)
        self.ui.comboBox_emprunt.currentTextChanged.connect(self.afficher_information)

        for e in self.isimm.empruntes:
            self.ui.comboBox_emprunt.addItem(str(e.numero_inscription)+" "+str(e.reference))

    def Retourner_emprunt(self):
        ch=self.ui.comboBox_emprunt.currentText().split(" ")
        print(self.isimm.empruntes)
        num = ch[0]
        ref=ch[1]
        self.isimm.retourner_emprunt(ref)
        self.showDialog("succès", "Retour terminé", True)



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
        self.ui.dateEdit_2.setDate(emprunt.date_retour)

