from PYConverted.Supprimer_etudiant import Ui_Dialog
from PyQt5.QtWidgets import *
class SupprimerEtudiant :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Supprimer.clicked.connect(self.Supprimer_etudiant)

        self.ui.radioButton.clicked.connect(self.radio_clicked)
        self.ui.radioButton_2.clicked.connect(self.radio_clicked)
        self.ui.radioButton_3.clicked.connect(self.radio_clicked)
        self.ui.radioButton_4.clicked.connect(self.radio_clicked)
        #INIT COMBO
        for e in self.isimm.etudiants:
            self.ui.comboBox_etudiant.addItem(str(e.numero_inscription)+" "+e.nom+" "+e.prenom)
        #visibility
        self.ui.comboBox_etudiant.setVisible(True)
        self.ui.comboBox_etudiant_section.setVisible(False)
        self.ui.comboBox_niveau.setVisible(False)
        self.ui.comboBox_section2.setVisible(False)
        self.ui.comboBox_niveau2.setVisible(False)

    def Supprimer_etudiant(self):
        if(self.ui.radioButton.isChecked()):
            print(self.isimm.etudiants)
            num=self.ui.comboBox_etudiant.currentText().split(" ")[0]
            self.isimm.supprimer_etudiant(num)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.etudiants)
            self.ui.comboBox_etudiant.clear()
            for e in self.isimm.etudiants:
                self.ui.comboBox_etudiant.addItem(str(e.numero_inscription) + " " + e.nom + " " + e.prenom)



        if (self.ui.radioButton_2.isChecked()):
            print(self.isimm.etudiants)

            section = self.ui.comboBox_etudiant_section.currentText()
            self.isimm.supprimer_etudiant_section(section)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.etudiants)
            self.ui.comboBox_etudiant.clear()
            for e in self.isimm.etudiants:
                self.ui.comboBox_etudiant.addItem(str(e.numero_inscription) + " " + e.nom + " " + e.prenom)
        if (self.ui.radioButton_3.isChecked()):
            print(self.isimm.etudiants)
            niveau = self.ui.comboBox_niveau.currentText()
            self.isimm.supprimer_etudiant_niveau(niveau)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.etudiants)
            self.ui.comboBox_etudiant.clear()
            for e in self.isimm.etudiants:
                self.ui.comboBox_etudiant.addItem(str(e.numero_inscription) + " " + e.nom + " " + e.prenom)
        if (self.ui.radioButton_4.isChecked()):
            print(self.isimm.etudiants)
            section = self.ui.comboBox_section2.currentText()
            niveau=self.ui.comboBox_niveau2.currentText()
            self.isimm.supprimer_etudiant_niveau_section(niveau,section)
            self.showDialog("succès", "Suppression terminé", True)
            print(self.isimm.etudiants)
            self.ui.comboBox_etudiant.clear()
            for e in self.isimm.etudiants:
                self.ui.comboBox_etudiant.addItem(str(e.numero_inscription) + " " + e.nom + " " + e.prenom)
    def radio_clicked(self):
        if(self.ui.radioButton.isChecked()):
            self.ui.comboBox_etudiant.setVisible(True)
            self.ui.comboBox_etudiant_section.setVisible(False)
            self.ui.comboBox_niveau.setVisible(False)
            self.ui.comboBox_section2.setVisible(False)
            self.ui.comboBox_niveau2.setVisible(False)
        if (self.ui.radioButton_2.isChecked()):
            self.ui.comboBox_etudiant.setVisible(False)
            self.ui.comboBox_etudiant_section.setVisible(True)
            self.ui.comboBox_niveau.setVisible(False)
            self.ui.comboBox_section2.setVisible(False)
            self.ui.comboBox_niveau2.setVisible(False)
        if (self.ui.radioButton_3.isChecked()):
            self.ui.comboBox_etudiant.setVisible(False)
            self.ui.comboBox_etudiant_section.setVisible(False)
            self.ui.comboBox_niveau.setVisible(True)
            self.ui.comboBox_section2.setVisible(False)
            self.ui.comboBox_niveau2.setVisible(False)
        if (self.ui.radioButton_4.isChecked()):
            self.ui.comboBox_etudiant.setVisible(False)
            self.ui.comboBox_etudiant_section.setVisible(False)
            self.ui.comboBox_niveau.setVisible(False)
            self.ui.comboBox_section2.setVisible(True)
            self.ui.comboBox_niveau2.setVisible(True)

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