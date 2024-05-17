

from PYConverted.Modifier_etudiant import Ui_Dialog
from PyQt5.QtWidgets import *

class ModifierEtudiant :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm = isimm
        self.ui.Modifier.clicked.connect(self.Modifier_etudiant)
        self.ui.comboBox_etudiant.currentTextChanged.connect(self.afficher_information)

        for e in self.isimm.etudiants:
            self.ui.comboBox_etudiant.addItem(str(e.numero_inscription)+" "+e.nom+" "+e.prenom)

    def Modifier_etudiant(self):
        ch=self.ui.comboBox_etudiant.currentText().split(" ")
        print(self.isimm.etudiants)
        num = ch[0]
        adresse=self.ui.edit_adresse.text()
        mail=self.ui.edit_mail.text()
        tel=self.ui.edit_telephone.text()
        # controle de saisie
        if(mail.count("@")!=1 or mail.find(".")==-1 or mail==""):
            self.showDialog("ereur", "mail non valide", False)
            return
        if (not tel.isnumeric() or tel == "" or len(tel) != 8):
            self.showDialog("ereur", "numero de téléphone non valide", False)
            return
        self.isimm.modifier_etudiant(num,adresse,mail,tel)
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
        num_insc=self.ui.comboBox_etudiant.currentText().split(" ")[0]
        etudiant=self.isimm.recherche_etudiant(num_insc)
        self.ui.edit_adresse.setText(etudiant.adresse)
        self.ui.edit_mail.setText(etudiant.mail)
        self.ui.edit_telephone.setText(str(etudiant.tel))
