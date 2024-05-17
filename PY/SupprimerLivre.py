from PYConverted.Supprimer_livre import Ui_Dialog
from PyQt5.QtWidgets import *
class SupprimerLivre :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Supprimer.clicked.connect(self.Supprimer_livre)

        self.ui.radioButton.clicked.connect(self.radio_clicked)
        self.ui.radioButton_2.clicked.connect(self.radio_clicked)
        self.ui.radioButton_3.clicked.connect(self.radio_clicked)
        #INIT COMBO
        for l in self.isimm.livres:
            self.ui.comboBox_livre.addItem(str(l.reference)+" "+l.titre)
        #visibility
        self.ui.comboBox_livre.setVisible(True)
        self.ui.supprimer_auteur.setVisible(False)
        self.ui.supprimer_annee.setVisible(False)

    def Supprimer_livre(self):
        if(self.ui.radioButton.isChecked()):
            print(self.isimm.livres)
            ref=self.ui.comboBox_livre.currentText().split(" ")[0]
            self.isimm.supprimer_livre(ref)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.livres)
            self.ui.comboBox_livre.clear()
            for l in self.isimm.livres:
                self.ui.comboBox_livre.addItem(str(l.reference)+" "+l.titre)

        if (self.ui.radioButton_2.isChecked()):
            print(self.isimm.livres)

            auteur = self.ui.supprimer_auteur.text()
            if (not self.isimm.recherche_livre_par_auteur(auteur)):
                self.showDialog("ereur", "il n'y a aucun livre écrit par ce auteur", False)
                return
            self.isimm.supprimer_livre_auteur(auteur)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.livres)
            self.ui.comboBox_livre.clear()
            for l in self.isimm.livres:
                self.ui.comboBox_livre.addItem(str(l.reference) + " " + l.titre)
        if (self.ui.radioButton_3.isChecked()):
            print(self.isimm.livres)
            annee = self.ui.supprimer_annee.text()
            if (not self.isimm.recherche_livre_par_annee(annee)):
                self.showDialog("ereur", "il n'y a aucun livre écrit dans cette année ", False)
                return
            self.isimm.supprimer_livre_annee(annee)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.livres)
            self.ui.comboBox_livre.clear()
            for l in self.isimm.livres:
                self.ui.comboBox_livre.addItem(str(l.reference) + " " + l.titre)
    def radio_clicked(self):
        if(self.ui.radioButton.isChecked()):
            self.ui.comboBox_livre.setVisible(True)
            self.ui.supprimer_auteur.setVisible(False)
            self.ui.supprimer_annee.setVisible(False)
        if (self.ui.radioButton_2.isChecked()):
            self.ui.comboBox_livre.setVisible(False)
            self.ui.supprimer_auteur.setVisible(True)
            self.ui.supprimer_annee.setVisible(False)
        if (self.ui.radioButton_3.isChecked()):
            self.ui.comboBox_livre.setVisible(False)
            self.ui.supprimer_auteur.setVisible(False)
            self.ui.supprimer_annee.setVisible(True)

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