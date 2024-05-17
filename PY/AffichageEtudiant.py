from PY.Etudiant import Etudiant
from PYConverted.Affichage_etudiant import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns = ["N inscription", "Nom", "Prenom", "Date de Naissance", "Adresse", "Mail", "Telephone",
                        "Section", "Niveau"]

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
        return 9
class AffichageEtudiant:
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm

        alternative = []
        for etudiant in self.isimm.etudiants:
            alternative.append(
                [etudiant.numero_inscription, etudiant.nom, etudiant.prenom, etudiant.date_naissance, etudiant.adresse, etudiant.mail,
                 etudiant.tel, etudiant.section, etudiant.niveau_etude])

        self.modal = TableModel(alternative)

        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.vertical_header = self.ui.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)

