from PY.Emprunt import Emprunt
from PYConverted.Ajout_emprunt import Ui_Dialog
from PyQt5.QtWidgets import *

class AjoutEmprunt :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Ajouter.clicked.connect(self.Ajouter_emprunt)
        for e in self.isimm.etudiants:
            self.ui.comboBox_etudiant.addItem(str(e.numero_inscription)+" "+e.nom+" "+e.prenom)
        for l in self.isimm.livres:
            self.ui.comboBox_livre.addItem(str(l.reference)+" "+l.titre+" "+l.nom_prenom_auteur)

    def Ajouter_emprunt(self):
        numero_inscription = self.ui.comboBox_etudiant.currentText().split(" ")[0]
        reference = self.ui.comboBox_livre.currentText().split(" ")[0]
        date_emprunt = self.ui.dateEdit.date()
        date_retour = self.ui.dateEdit_2.date()
        #control de saisie
        if (self.isimm.recherche_emprunt_pour_supprimer(numero_inscription,reference)):
            self.showDialog("ereur", "Emprunt exisste déja", False)
            return
        if(date_retour<=date_emprunt):
            self.showDialog("ereur", "La date de retour doit être superieur â celle d'emprunt", False)
            return

        l=self.isimm.recherche_livre(reference)
        if l:
            nombre_exp=l.nombre_exp
            if(int(nombre_exp)>0):
                print(numero_inscription, reference, date_emprunt, date_retour)

                print(self.isimm.empruntes)
                new_emprunt = Emprunt(numero_inscription, reference, date_emprunt, date_retour)

                self.isimm.ajouter_emprunt(new_emprunt)
                print(self.isimm.empruntes)
                self.showDialog("succès", "emprunt ajouté", True)
                x=int(l.nombre_exp)
                x=x-1
                l.nombre_exp=str(x)
            else:
                self.showDialog("ereur", "Ce livre n'est pas disponible", False)


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
