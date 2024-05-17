from PY.Livre import Livre
from PYConverted.Recherche_livre import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns = ["Reference", "titre", "nom et prenom d'auteur", "année d'edition", "nombre d'exemplaire"]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return 5
class RechercheLivre :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Rechercher.clicked.connect(self.Rechercher_livre)

        self.ui.radioButton.clicked.connect(self.radio_clicked)
        self.ui.radioButton_2.clicked.connect(self.radio_clicked)
        self.ui.radioButton_3.clicked.connect(self.radio_clicked)
        self.ui.radioButton_4.clicked.connect(self.radio_clicked)

        self.ui.edit_reference.setVisible(True)
        self.ui.edit_titre.setVisible(False)
        self.ui.edit_annee.setVisible(False)
        self.ui.edit_auteur.setVisible(False)
    def verifier_chaine(self,ch):
        for i in ch:
            if(not i.isalpha() and i!=" " and i!="'"):
                return False
        return True
    def radio_clicked(self):
        if (self.ui.radioButton.isChecked()):
            self.ui.edit_reference.setVisible(True)
            self.ui.edit_titre.setVisible(False)
            self.ui.edit_annee.setVisible(False)
            self.ui.edit_auteur.setVisible(False)
        if (self.ui.radioButton_2.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_titre.setVisible(True)
            self.ui.edit_annee.setVisible(False)
            self.ui.edit_auteur.setVisible(False)
        if (self.ui.radioButton_3.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_titre.setVisible(False)
            self.ui.edit_annee.setVisible(True)
            self.ui.edit_auteur.setVisible(False)

        if (self.ui.radioButton_4.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_titre.setVisible(False)
            self.ui.edit_annee.setVisible(False)
            self.ui.edit_auteur.setVisible(True)


    def Rechercher_livre(self):
        alternative = []
        if (self.ui.radioButton.isChecked()):
            ref=self.ui.edit_reference.text()
            if (len(ref) != 5 or not ref.isnumeric()):
                self.showDialog("ereur", "reference non valide", False)
                return
            livre=self.isimm.recherche_livre(ref)
            if(livre):
                alternative.append(
                    [livre.reference, livre.titre, livre.nom_prenom_auteur, livre.anne_edition, livre.nombre_exp])
            else:
                self.showDialog("ereur", "livre inexistant", False)
                return



        if (self.ui.radioButton_2.isChecked()):
            titre=self.ui.edit_titre.text()
            if (not self.verifier_chaine(titre)):
                self.showDialog("ereur", "titre non valide", False)
                return
            for livre in self.isimm.livres:
                if(livre.titre==titre):
                    alternative.append(
                        [livre.reference, livre.titre, livre.nom_prenom_auteur, livre.anne_edition, livre.nombre_exp])

        if (self.ui.radioButton_3.isChecked()):
            annee=self.ui.edit_annee.text()
            if (int(annee) < 1800 or not annee.isnumeric()):
                self.showDialog("ereur", "année invalide", False)
                return
            livre = self.isimm.recherche_livre_par_annee(annee)
            if (livre):
                alternative.append(
                    [livre.reference, livre.titre, livre.nom_prenom_auteur, livre.anne_edition, livre.nombre_exp])
            else:
                self.showDialog("ereur", "livres inexistants", False)
                return


        if (self.ui.radioButton_4.isChecked()):
            auteur = self.ui.edit_auteur.text()
            for livre in self.isimm.livres:
                if(livre.nom_prenom_auteur==auteur ):
                    alternative.append(
                        [livre.reference, livre.titre, livre.nom_prenom_auteur, livre.anne_edition, livre.nombre_exp])



        self.modal = TableModel(alternative)

        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.vertical_header = self.ui.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
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