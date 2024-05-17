from PY.Etudiant import Etudiant
from PYConverted.Recherche_etudiant import Ui_Dialog
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
class RechercheEtudiant :
    def __init__(self,isimm):
        self.window=QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.window)
        self.isimm=isimm
        self.ui.Rechercher.clicked.connect(self.Rechercher_etudiant)

        self.ui.radioButton.clicked.connect(self.radio_clicked)
        self.ui.radioButton_2.clicked.connect(self.radio_clicked)
        self.ui.radioButton_3.clicked.connect(self.radio_clicked)
        self.ui.radioButton_4.clicked.connect(self.radio_clicked)

        self.ui.edit_numero_insc.setVisible(True)
        self.ui.comboBox_etudiant_section.setVisible(False)
        self.ui.comboBox_niveau.setVisible(False)
        self.ui.comboBox_section2.setVisible(False)
        self.ui.comboBox_niveau2.setVisible(False)

    def radio_clicked(self):
        if (self.ui.radioButton.isChecked()):
            self.ui.edit_numero_insc.setVisible(True)
            self.ui.comboBox_etudiant_section.setVisible(False)
            self.ui.comboBox_niveau.setVisible(False)
            self.ui.comboBox_section2.setVisible(False)
            self.ui.comboBox_niveau2.setVisible(False)
        if (self.ui.radioButton_2.isChecked()):
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.comboBox_etudiant_section.setVisible(True)
            self.ui.comboBox_niveau.setVisible(False)
            self.ui.comboBox_section2.setVisible(False)
            self.ui.comboBox_niveau2.setVisible(False)
        if (self.ui.radioButton_3.isChecked()):
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.comboBox_etudiant_section.setVisible(False)
            self.ui.comboBox_niveau.setVisible(True)
            self.ui.comboBox_section2.setVisible(False)
            self.ui.comboBox_niveau2.setVisible(False)
        if (self.ui.radioButton_4.isChecked()):
            self.ui.edit_numero_insc.setVisible(False)
            self.ui.comboBox_etudiant_section.setVisible(False)
            self.ui.comboBox_niveau.setVisible(False)
            self.ui.comboBox_section2.setVisible(True)
            self.ui.comboBox_niveau2.setVisible(True)

    def Rechercher_etudiant(self):
        alternative = []
        if (self.ui.radioButton.isChecked()):
            num_insc=self.ui.edit_numero_insc.text()
            if (len(num_insc) != 6 or not num_insc.isnumeric()):
                self.showDialog("ereur", "numero d'inscription non valide", False)
                return
            etudiant=self.isimm.recherche_etudiant(num_insc)
            if(etudiant):
                alternative.append(
                    [etudiant.numero_inscription, etudiant.nom, etudiant.prenom, etudiant.date_naissance, etudiant.adresse,
                     etudiant.mail,
                     etudiant.tel, etudiant.section, etudiant.niveau_etude])


        if (self.ui.radioButton_2.isChecked()):
            section=self.ui.comboBox_etudiant_section.currentText()
            for etudiant in self.isimm.etudiants:
                if(etudiant.section==section):
                    alternative.append(
                        [etudiant.numero_inscription, etudiant.nom, etudiant.prenom, etudiant.date_naissance, etudiant.adresse,
                         etudiant.mail,
                         etudiant.tel, etudiant.section, etudiant.niveau_etude])


        if (self.ui.radioButton_3.isChecked()):
            niveau=self.ui.comboBox_niveau.currentText()
            for etudiant in self.isimm.etudiants:
                if(etudiant.niveau_etude==niveau):
                    alternative.append(
                        [etudiant.numero_inscription, etudiant.nom, etudiant.prenom, etudiant.date_naissance, etudiant.adresse,
                         etudiant.mail,
                         etudiant.tel, etudiant.section, etudiant.niveau_etude])

        if (self.ui.radioButton_4.isChecked()):
            section = self.ui.comboBox_section2.currentText()
            niveau = self.ui.comboBox_niveau2.currentText()
            for etudiant in self.isimm.etudiants:
                if(etudiant.niveau_etude==niveau and etudiant.section==section):
                    alternative.append(
                        [etudiant.numero_inscription, etudiant.nom, etudiant.prenom, etudiant.date_naissance, etudiant.adresse,
                         etudiant.mail,
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