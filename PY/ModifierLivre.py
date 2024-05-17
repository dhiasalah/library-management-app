from PYConverted.Modifier_livre import Ui_Dialog
from PyQt5.QtWidgets import *

class ModifierLivre :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm = isimm
        self.ui.Modifier.clicked.connect(self.Modifier_livre)
        self.ui.comboBox_livre.currentTextChanged.connect(self.afficher_information)

        for l in self.isimm.livres:
            self.ui.comboBox_livre.addItem(str(l.reference)+"/"+l.titre+"/"+l.nom_prenom_auteur)

    def Modifier_livre(self):
        ch=self.ui.comboBox_livre.currentText().split("/")
        print(self.isimm.livres)
        ref = ch[0]
        nombre_exp=self.ui.edit_nombre_exp.text()
        # controle de saisie
        if(not nombre_exp.isnumeric() or nombre_exp=="" ):
            self.showDialog("ereur", "nombre d'exemplaire non valide", False)
            return
        self.isimm.modifier_livre(ref,nombre_exp)
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
        ref=self.ui.comboBox_livre.currentText().split("/")[0]
        livre=self.isimm.recherche_livre(ref)
        self.ui.edit_nombre_exp.setText(livre.nombre_exp)
