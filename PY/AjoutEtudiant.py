from PY.Etudiant import Etudiant
from PYConverted.Ajout_etudiant import Ui_Dialog
from PyQt5.QtWidgets import *

class AjoutEtudiant :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Ajouter.clicked.connect(self.Ajouter_etudiant)
    def verifier_chaine(self, ch):
        for i in ch:
            if (not i.isalpha() and i != " "):
                return False
        return True

    def Ajouter_etudiant(self):
        numero_inscription = self.ui.edit_numero_inscription.text()
        nom = self.ui.edit_nom.text()
        prenom = self.ui.edit_prenom.text()
        date_naissance = self.ui.date_naissance.date()
        adresse=self.ui.edit_adresse.text()
        mail=self.ui.edit_mail.text()
        tel=self.ui.edit_telephone.text()
        section=self.ui.comboBox.currentText()
        niveau_etude=self.ui.edit_niveau.text()



        # controle de saisie
        if(self.isimm.recherche_etudiant(numero_inscription)):
            self.showDialog("ereur", "etudiant exisste déja", False)
            self.ui.edit_numero_inscription.clear()
            return
        if (len(numero_inscription) != 6 or not numero_inscription.isnumeric()):
            self.showDialog("ereur", "numero d'inscription non valide", False)
            self.ui.edit_numero_inscription.clear()
            return
        if (not self.verifier_chaine(nom)):
            self.showDialog("ereur", "nom non valide", False)
            self.ui.edit_nom.clear()
            return
        if (not self.verifier_chaine(prenom)):
            self.showDialog("ereur", "prenom non valide", False)
            self.ui.edit_prenom.clear()
            return
        if (date_naissance.year() > 2004):
            self.showDialog("ereur", "date invalide", False)
            return
        if(mail.count("@")!=1 or mail.find(".")==-1 or mail==""):
            self.showDialog("ereur", "mail non valide", False)
            self.ui.edit_mail.clear()
            return
        if(not tel.isnumeric() or tel=="" or len(tel)!=8):
            self.showDialog("ereur", "numero de téléphone non valide", False)
            self.ui.edit_telephone.clear()
            return
        if(not niveau_etude.isnumeric() or int(niveau_etude)<=0 or int(niveau_etude) not in {1,2,3}):
            self.showDialog("ereur", "niveau non valide", False)
            self.ui.edit_niveau.clear()
            return
        if(section=="CPI-cycle preparatoire integree" and int(niveau_etude)>2):
            self.showDialog("ereur", "niveau non valide", False)
            self.ui.edit_niveau.clear()
            return
        print(numero_inscription,nom,prenom,date_naissance,adresse,mail,tel,section,niveau_etude)

        print(self.isimm.etudiants)
        new_etudiant = Etudiant(numero_inscription, nom, prenom,date_naissance,adresse,mail,tel,section,niveau_etude)
        self.isimm.ajouter_etudiant(new_etudiant)
        print(self.isimm.etudiants)
        self.showDialog("succès", "étudiant ajouté", True)

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
