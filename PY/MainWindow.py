import os

from PyQt5.QtCore import QDate


from PYConverted.Main_window import Ui_MainWindow
from PyQt5.QtWidgets import *

from .AffichageEmprunt import AffichageEmprunt
from .AffichageEtudiant import AffichageEtudiant
from .AffichageLivre import AffichageLivre
from .AjoutEmprunt import AjoutEmprunt
from .AjoutEtudiant import AjoutEtudiant
from .AjoutLivre import AjoutLivre
from .Emprunt import Emprunt
from .Etudiant import Etudiant
from .ISIMM import ISIMM
from .Livre import Livre
from .ModifierEmprunt import ModifierEmprunt
from .ModifierEtudiant import ModifierEtudiant
from .ModifierLivre import ModifierLivre
from .RechercheEmprunt import RechercheEmprunt
from .RechercheEtudiant import RechercheEtudiant
from .RetourEmprunt import RetourEmprunt
from .SupprimerEmprunt import SupprimerEmprunt
from .SupprimerEtudiant import SupprimerEtudiant
from .SupprimerLivre import SupprimerLivre
from .RechercheLivre import RechercheLivre
from .MainWindowPicture import MainWindowPicture

class MainWindow:
    def __init__(self):
        self.window=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.DataRecovered = False
        self.isimm=ISIMM()


        self.ui.actionAjouter_un_tudiant.triggered.connect(self.redirect_ajout_etudiant)
        self.ui.actionSupprimer_un_tudiant.triggered.connect(self.redirect_supprimer_etudiant)
        self.ui.actionModifier_un_tudiant.triggered.connect(self.redirect_modifier_etudiant)
        self.ui.actionAjouter_un_livre.triggered.connect(self.redirect_ajout_livre)
        self.ui.actionSupprimer_un_livre.triggered.connect(self.redirect_supprimer_livre)
        self.ui.actionAfficher_les_tudiants.triggered.connect(self.redirect_afficher_etudiant)
        self.ui.actionEnregistrement.triggered.connect(self.enregistrer)
        self.ui.actionR_cup_ration.triggered.connect(self.recuperer)
        self.ui.actionRechercher_tudiant.triggered.connect(self.redirect_rechercher_etudiant)
        self.ui.actionModifier_un_livre.triggered.connect(self.redirect_modifier_livre)
        self.ui.actionAfficher_les_livres.triggered.connect(self.redirect_afficher_livre)
        self.ui.actionRechercher_livre.triggered.connect(self.redirect_rechercher_livre)
        self.ui.actionAjouter_des_empruntes.triggered.connect(self.redirect_ajout_emprunt)
        self.ui.actionRetour_des_empruntes.triggered.connect(self.redirect_retour_emprunt)
        self.ui.actionSupprimer_des_empruntes.triggered.connect(self.redirect_supprimer_emprunt)
        self.ui.actionModifier_des_empruntes.triggered.connect(self.redirect_modifier_emprunt)
        self.ui.actionAfficher_emprunte.triggered.connect(self.redirect_afficher_emprunt)
        self.ui.actionRecherche_emprunte_par_date.triggered.connect(self.redirect_rechercher_emprunt)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionAcceuil.triggered.connect(self.acceuil)
        self.ui.actionEnonc_projet.triggered.connect(self.ouvrirEnonce)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.Main = MainWindowPicture(self.isimm)
        self.ui.stackedWidget.addWidget(self.Main.window)
        self.ui.stackedWidget.setCurrentWidget(self.Main.window)



    def ouvrirEnonce(self):
        os.system(".\CSV\Enonce.pdf")

    def acceuil(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.Main = MainWindowPicture(self.isimm)
        self.ui.stackedWidget.addWidget(self.Main.window)
        self.ui.stackedWidget.setCurrentWidget(self.Main.window)

    def exit(self):
        self.window.close()
        
    def redirect_ajout_etudiant(self):
        if(self.DataRecovered ):
            self.Ajout=AjoutEtudiant(self.isimm)
            self.ui.stackedWidget.addWidget(self.Ajout.window)
            self.ui.stackedWidget.setCurrentWidget(self.Ajout.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)
    def redirect_supprimer_etudiant(self):
        if (self.DataRecovered):
            self.Supprimer=SupprimerEtudiant(self.isimm)
            self.ui.stackedWidget.addWidget(self.Supprimer.window)
            self.ui.stackedWidget.setCurrentWidget(self.Supprimer.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données", False)
    def redirect_modifier_etudiant(self):
        if (self.DataRecovered):
            self.Modifier = ModifierEtudiant(self.isimm)
            self.ui.stackedWidget.addWidget(self.Modifier.window)
            self.ui.stackedWidget.setCurrentWidget(self.Modifier.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def redirect_afficher_etudiant(self):
        if (self.DataRecovered):
            self.Afficher=AffichageEtudiant(self.isimm)
            self.ui.stackedWidget.addWidget(self.Afficher.window)
            self.ui.stackedWidget.setCurrentWidget(self.Afficher.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)
    def redirect_rechercher_etudiant(self):
        if (self.DataRecovered):
            self.Rechercher=RechercheEtudiant(self.isimm)
            self.ui.stackedWidget.addWidget(self.Rechercher.window)
            self.ui.stackedWidget.setCurrentWidget(self.Rechercher.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def parseStudent(self, line):
        lis = line.split(",")
        lis[8] = lis[8].replace("\n", "")
        dt = str(lis[3]).split("/")
        dat = QDate(int(dt[0]), int(dt[1]), int(dt[2]))
        return Etudiant(lis[0], lis[1], lis[2], dat, lis[4], lis[5], lis[6], lis[7], lis[8])
    def enregistrer(self):
        if (self.DataRecovered):
            self.enregistrerEtudiant()
            self.enregistrerLivre()
            self.enregistrerEmprunt()
            self.showDialog("succèe", "Enregistrement terminé", True)

        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données", False)


    def recuperer(self):
        self.recupererEtudiant()
        self.recupererLivre()
        self.recupererEmprunt()
        self.showDialog("succèe", "Recupération terminé", True)
        self.DataRecovered = True
    def enregistrerEtudiant(self):
        F = open("CSV/Etudiants.csv", "w+")
        F.seek(0)
        F.write("Numero d'inscription,Nom,Prenom,Date de naissance,Adresse,Mail,Telephone,Section,Niveau d'etude\n")
        for i in self.isimm.etudiants:
            found = False
            for j in F:
                numI = j.split(",")[0]
                if (numI == i.numero_inscription):
                    found = True
                    break
            if (not found):
                F.write(i.numero_inscription + "," + i.nom + "," + i.prenom + "," + str(i.date_naissance.year()) + "/" + str(
                    i.date_naissance.month()) + "/" + str(
                    i.date_naissance.day()) + "," + i.adresse + "," + i.mail + "," + i.tel + "," + i.section + "," + i.niveau_etude + "\n")

        F.close()

    def recupererEtudiant(self):
        self.isimm.etudiants.clear()
        F = open("CSV/Etudiants.csv", "r")
        count = -1
        for line in F:
            count += 1
            if (count == 0):
                continue
            self.isimm.etudiants.append(self.parseStudent(line))

        F.close()
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



    #livre
    def redirect_ajout_livre(self):
        if (self.DataRecovered):
            self.Ajout = AjoutLivre(self.isimm)
            self.ui.stackedWidget.addWidget(self.Ajout.window)
            self.ui.stackedWidget.setCurrentWidget(self.Ajout.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def redirect_supprimer_livre(self):
        if (self.DataRecovered):
            self.Supprimer = SupprimerLivre(self.isimm)
            self.ui.stackedWidget.addWidget(self.Supprimer.window)
            self.ui.stackedWidget.setCurrentWidget(self.Supprimer.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def redirect_modifier_livre(self):
        if (self.DataRecovered):
            self.Modifier = ModifierLivre(self.isimm)
            self.ui.stackedWidget.addWidget(self.Modifier.window)

            self.ui.stackedWidget.setCurrentWidget(self.Modifier.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)


    def redirect_afficher_livre(self):
        if (self.DataRecovered):
            self.Afficher=AffichageLivre(self.isimm)
            self.ui.stackedWidget.addWidget(self.Afficher.window)
            self.ui.stackedWidget.setCurrentWidget(self.Afficher.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def redirect_rechercher_livre(self):
        if (self.DataRecovered):
            self.Rechercher = RechercheLivre(self.isimm)
            self.ui.stackedWidget.addWidget(self.Rechercher.window)

            self.ui.stackedWidget.setCurrentWidget(self.Rechercher.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def parselivre(self, line):
        lis = line.split(",")
        lis[4] = lis[4].replace("\n", "")
        return Livre(lis[0], lis[1], lis[2], lis[3], lis[4])



    def enregistrerLivre(self):
        F = open("CSV/Livres.csv", "w+")
        F.seek(0)
        F.write("Reference,titre,nom et prenom d'auteur,année d'edition,nombre d'exemplaire\n")
        for i in self.isimm.livres:
            found = False
            for j in F:
                ref = j.split(",")[0]
                if (ref== i.reference):
                    found = True
                    break
            if (not found):
                F.write(i.reference + "," + i.titre + "," + i.nom_prenom_auteur+ "," +  i.anne_edition + "," + i.nombre_exp +"\n")

        F.close()

    def recupererLivre(self):
        self.isimm.livres.clear()
        F = open("CSV/Livres.csv", "r")
        count = -1
        for line in F:
            count += 1
            if (count == 0):
                continue
            self.isimm.livres.append(self.parselivre(line))

        F.close()

    #emprunt
    def redirect_ajout_emprunt(self):
        if (self.DataRecovered):
            self.Ajout = AjoutEmprunt(self.isimm)
            self.ui.stackedWidget.addWidget(self.Ajout.window)

            self.ui.stackedWidget.setCurrentWidget(self.Ajout.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)
    def redirect_retour_emprunt(self):
        if (self.DataRecovered):
            self.Retour=RetourEmprunt(self.isimm)
            self.ui.stackedWidget.addWidget(self.Retour.window)

            self.ui.stackedWidget.setCurrentWidget(self.Retour.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def redirect_supprimer_emprunt(self):
        if (self.DataRecovered):
            self.Supprimer = SupprimerEmprunt(self.isimm)
            self.ui.stackedWidget.addWidget(self.Supprimer.window)
            self.ui.stackedWidget.setCurrentWidget(self.Supprimer.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)
    def redirect_modifier_emprunt(self):
        if (self.DataRecovered):
            self.Modifier = ModifierEmprunt(self.isimm)
            self.ui.stackedWidget.addWidget(self.Modifier.window)

            self.ui.stackedWidget.setCurrentWidget(self.Modifier.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)
    def redirect_afficher_emprunt(self):
        if (self.DataRecovered):
            self.Afficher=AffichageEmprunt(self.isimm)
            self.ui.stackedWidget.addWidget(self.Afficher.window)
            self.ui.stackedWidget.setCurrentWidget(self.Afficher.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)
    def redirect_rechercher_emprunt(self):
        if (self.DataRecovered):
            self.Rechercher = RechercheEmprunt(self.isimm)
            self.ui.stackedWidget.addWidget(self.Rechercher.window)
            self.ui.stackedWidget.setCurrentWidget(self.Rechercher.window)
        else:
            self.showDialog("Invalid Action", "Vous devez recuperer vos données",False)

    def parseemprunt(self, line):
        lis = line.split(",")
        lis[3] = lis[3].replace("\n", "")
        dt = str(lis[2]).split("/")
        dt2=str(lis[3]).split("/")
        dat = QDate(int(dt[0]), int(dt[1]), int(dt[2]))
        dat2=QDate(int(dt2[0]), int(dt2[1]), int(dt2[2]))
        return Emprunt(lis[0], lis[1], dat,dat2)

    def enregistrerEmprunt(self):
        F = open("CSV/Emprunts.csv", "w+")
        F.seek(0)
        F.write("numero d'inscription,reference de livre,date d'emprunt,date de retour\n")
        for i in self.isimm.empruntes:
            found = False
            for j in F:
                numI = j.split(",")[0]
                if (numI == i.numero_inscription):
                    found = True
                    break
            if (not found):
                F.write(i.numero_inscription + "," + i.reference + ","  + str(
                    i.date_emprunt.year()) + "/" + str(
                    i.date_emprunt.month()) + "/" + str(
                    i.date_emprunt.day()) + ',' +str(
                    i.date_retour.year()) + "/" + str(
                    i.date_retour.month()) + "/" + str(
                    i.date_retour.day())  +"\n")

        F.close()

    def recupererEmprunt(self):
        self.isimm.empruntes.clear()
        F = open("CSV/Emprunts.csv", "r")
        count = -1
        for line in F:
            count += 1
            if (count == 0):
                continue
            self.isimm.empruntes.append(self.parseemprunt(line))

        F.close()
