from PYConverted.Supprimer_emprunt import Ui_Dialog
from PyQt5.QtWidgets import *
class SupprimerEmprunt :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Supprimer.clicked.connect(self.Supprimer_emprunt)

        #INIT COMBO
        for e in self.isimm.empruntes:
            l = self.isimm.recherche_livre(e.reference)
            self.ui.comboBox_emprunt.addItem(str(e.numero_inscription) + " " + str(e.reference) + " " + l.titre)


    def Supprimer_emprunt(self):
            print(self.isimm.empruntes)
            num=self.ui.comboBox_emprunt.currentText().split(" ")[0]
            ref=self.ui.comboBox_emprunt.currentText().split(" ")[1]
            self.isimm.supprimer_emprunt(num,ref)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.empruntes)
            self.ui.comboBox_emprunt.clear()
            for e in self.isimm.empruntes:
                l=self.isimm.recherche_livre(e.reference)
                self.ui.comboBox_emprunt.addItem(str(e.numero_inscription)+" "+str(e.reference)+" "+l.titre)


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