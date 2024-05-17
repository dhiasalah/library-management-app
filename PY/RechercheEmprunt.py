from PY.Etudiant import Etudiant
from PYConverted.Recherche_emprunt import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.columns = ["numero d'inscription","reference de livre","date d'emprunt","date de retour"]

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
        return 4
class RechercheEmprunt :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Rechercher.clicked.connect(self.Rechercher_emprunt)

        self.ui.radioButton.clicked.connect(self.radio_clicked)
        self.ui.radioButton_2.clicked.connect(self.radio_clicked)
        self.ui.radioButton_3.clicked.connect(self.radio_clicked)
        self.ui.radioButton_4.clicked.connect(self.radio_clicked)
        self.ui.radioButton_5.clicked.connect(self.radio_clicked)
        self.ui.radioButton_6.clicked.connect(self.radio_clicked)

        self.ui.edit_reference.setVisible(True)
        self.ui.edit_numero_insc.setVisible(False)
        self.ui.dateEdit.setVisible(False)
        self.ui.dateEdit_2.setVisible(False)
        self.ui.dateEdit_3.setVisible(False)
        self.ui.dateEdit_4.setVisible(False)
        self.ui.dateEdit_5.setVisible(False)
        self.ui.dateEdit_6.setVisible(False)

    def radio_clicked(self):
        if (self.ui.radioButton.isChecked()):
            self.ui.edit_reference.setVisible(True)
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.dateEdit.setVisible(False)
            self.ui.dateEdit_2.setVisible(False)
            self.ui.dateEdit_3.setVisible(False)
            self.ui.dateEdit_4.setVisible(False)
            self.ui.dateEdit_5.setVisible(False)
            self.ui.dateEdit_6.setVisible(False)
        if (self.ui.radioButton_2.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_numero_insc.setVisible(True)
            self.ui.dateEdit.setVisible(False)
            self.ui.dateEdit_2.setVisible(False)
            self.ui.dateEdit_3.setVisible(False)
            self.ui.dateEdit_4.setVisible(False)
            self.ui.dateEdit_5.setVisible(False)
            self.ui.dateEdit_6.setVisible(False)
        if (self.ui.radioButton_3.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.dateEdit.setVisible(True)
            self.ui.dateEdit_2.setVisible(False)
            self.ui.dateEdit_3.setVisible(False)
            self.ui.dateEdit_4.setVisible(False)
            self.ui.dateEdit_5.setVisible(False)
            self.ui.dateEdit_6.setVisible(False)
        if (self.ui.radioButton_4.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.dateEdit.setVisible(False)
            self.ui.dateEdit_2.setVisible(True)
            self.ui.dateEdit_3.setVisible(False)
            self.ui.dateEdit_4.setVisible(False)
            self.ui.dateEdit_5.setVisible(False)
            self.ui.dateEdit_6.setVisible(False)
        if (self.ui.radioButton_5.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.dateEdit.setVisible(False)
            self.ui.dateEdit_2.setVisible(False)
            self.ui.dateEdit_3.setVisible(True)
            self.ui.dateEdit_4.setVisible(True)
            self.ui.dateEdit_5.setVisible(False)
            self.ui.dateEdit_6.setVisible(False)
        if (self.ui.radioButton_6.isChecked()):
            self.ui.edit_reference.setVisible(False)
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.dateEdit.setVisible(False)
            self.ui.dateEdit_2.setVisible(False)
            self.ui.dateEdit_3.setVisible(False)
            self.ui.dateEdit_4.setVisible(False)
            self.ui.dateEdit_5.setVisible(True)
            self.ui.dateEdit_6.setVisible(True)

    def Rechercher_emprunt(self):
        alternative = []
        if (self.ui.radioButton.isChecked()):
            ref=self.ui.edit_reference.text()
            emprunt=self.isimm.recherche_emprunt_par_ref(ref)
            if(emprunt):
                alternative.append(
                    [emprunt.numero_inscription,emprunt.reference, emprunt.date_emprunt, emprunt.date_retour])


        if (self.ui.radioButton_2.isChecked()):
            num_insc=self.ui.edit_numero_insc.text()
            emprunt = self.isimm.recherche_emprunt(num_insc)
            if (emprunt):
                alternative.append(
                    [emprunt.numero_inscription, emprunt.reference, emprunt.date_emprunt, emprunt.date_retour])


        if (self.ui.radioButton_3.isChecked()):
            date=self.ui.dateEdit.date()
            for emprunt in self.isimm.empruntes:
                if(emprunt.date_emprunt==date):
                    alternative.append(
                        [emprunt.numero_inscription, emprunt.reference, emprunt.date_emprunt, emprunt.date_retour])

        if (self.ui.radioButton_4.isChecked()):
            date = self.ui.dateEdit_2.date()
            for emprunt in self.isimm.empruntes:
                if (emprunt.date_retour == date):
                    alternative.append(
                        [emprunt.numero_inscription, emprunt.reference, emprunt.date_emprunt, emprunt.date_retour])
        if (self.ui.radioButton_5.isChecked()):
            date1 = self.ui.dateEdit_3.date()
            date2=self.ui.dateEdit_4.date()
            for emprunt in self.isimm.empruntes:
                if (emprunt.date_emprunt >= date1 and emprunt.date_emprunt<= date2):
                    alternative.append(
                        [emprunt.numero_inscription, emprunt.reference, emprunt.date_emprunt, emprunt.date_retour])


        if (self.ui.radioButton_6.isChecked()):
            date1 = self.ui.dateEdit_5.date()
            date2 = self.ui.dateEdit_6.date()
            for emprunt in self.isimm.empruntes:
                if (emprunt.date_retour >= date1 and emprunt.date_retour <= date2):
                    alternative.append(
                        [emprunt.numero_inscription, emprunt.reference, emprunt.date_emprunt, emprunt.date_retour])

        self.modal = TableModel(alternative)

        self.ui.tableView.setModel(self.modal)
        self.horizontal_header = self.ui.tableView.horizontalHeader()
        self.vertical_header = self.ui.tableView.verticalHeader()
        self.horizontal_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontal_header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontal_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
