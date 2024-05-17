from PY.Livre import Livre
from PYConverted.Ajout_livre import Ui_Dialog
from PyQt5.QtWidgets import *
class AjoutLivre :
    def __init__( self ,isimm):
        self.window = QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm = isimm
        self.ui.Ajouter.clicked.connect(self.Ajouter_livre)

    def verifier_chaine(self,ch):
        for i in ch:
            if(not i.isalpha() and i!=" " and i!="'"):
                return False
        return True
    def Ajouter_livre(self):
        reference = self.ui.edit_reference.text()
        titre = self.ui.edit_titre.text()
        nom_prenom_auteur = self.ui.edit_nom_prenom.text()
        anne_edition =self.ui.edit_annee_edition.text()
        nombre_exp=self.ui.edit_nombre_exp.text()

        # controle de saisie
        if (self.isimm.recherche_livre(reference)):
            self.showDialog("ereur", "livre exisste déja", False)
            return
        if (len(reference) != 5 or not reference.isnumeric()):
            self.showDialog("ereur", "reference non valide", False)
            return
        if (not self.verifier_chaine(titre)):
            self.showDialog("ereur", "titre non valide", False)
            return
        if (not self.verifier_chaine(nom_prenom_auteur)):
            self.showDialog("ereur", "non et prenom non valide", False)
            return
        if (not anne_edition.isnumeric() or int(anne_edition) < 1800  ):
            self.showDialog("ereur", "année invalide", False)
            return
        if (not nombre_exp.isdecimal() or int(nombre_exp)<=0):
            self.showDialog("ereur", "nombre d'exemplaires invalide", False)
            return

        print(reference,titre,nom_prenom_auteur,anne_edition,nombre_exp)

        print(self.isimm.livres)
        new_livre = Livre(reference,titre,nom_prenom_auteur,anne_edition,nombre_exp)
        self.isimm.ajouter_livre(new_livre)
        print(self.isimm.livres)
        self.showDialog("succès", "livre ajouté", True)

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

