# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1199, 799)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("font: 75 16pt \"Cambria\";\n"
"background-color: rgb(0, 170, 255);\n"
"color: BLACK;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.centralwidget.setFont(font)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1199, 38))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGestion_des_tudiants = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_tudiants.setObjectName("menuGestion_des_tudiants")
        self.menuMise_jour_des_tudiants = QtWidgets.QMenu(self.menuGestion_des_tudiants)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.menuMise_jour_des_tudiants.setFont(font)
        self.menuMise_jour_des_tudiants.setObjectName("menuMise_jour_des_tudiants")
        self.menuRecherche_et_affichage = QtWidgets.QMenu(self.menuGestion_des_tudiants)
        self.menuRecherche_et_affichage.setObjectName("menuRecherche_et_affichage")
        self.menuGestion_des_Livres = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_Livres.setObjectName("menuGestion_des_Livres")
        self.menuMise_jour_des_livres = QtWidgets.QMenu(self.menuGestion_des_Livres)
        self.menuMise_jour_des_livres.setObjectName("menuMise_jour_des_livres")
        self.menuRecherche_et_affichage_2 = QtWidgets.QMenu(self.menuGestion_des_Livres)
        self.menuRecherche_et_affichage_2.setObjectName("menuRecherche_et_affichage_2")
        self.menuGestion_des_emprunts = QtWidgets.QMenu(self.menubar)
        self.menuGestion_des_emprunts.setObjectName("menuGestion_des_emprunts")
        self.menuMise_jour_des_empruntes = QtWidgets.QMenu(self.menuGestion_des_emprunts)
        self.menuMise_jour_des_empruntes.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuMise_jour_des_empruntes.setObjectName("menuMise_jour_des_empruntes")
        self.menuRecherche_et_affichage_3 = QtWidgets.QMenu(self.menuGestion_des_emprunts)
        self.menuRecherche_et_affichage_3.setObjectName("menuRecherche_et_affichage_3")
        self.menuEnregistrement_et_r_cup_ration = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrement_et_r_cup_ration.setObjectName("menuEnregistrement_et_r_cup_ration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAcceuil = QtWidgets.QAction(MainWindow)
        self.actionAcceuil.setObjectName("actionAcceuil")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAjouter_un_tudiant = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_tudiant.setObjectName("actionAjouter_un_tudiant")
        self.actionSupprimer_un_tudiant = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_tudiant.setObjectName("actionSupprimer_un_tudiant")
        self.actionModifier_un_tudiant = QtWidgets.QAction(MainWindow)
        self.actionModifier_un_tudiant.setObjectName("actionModifier_un_tudiant")
        self.actionAfficher_les_tudiants = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_tudiants.setObjectName("actionAfficher_les_tudiants")
        self.actionRecherche_par_numero_d_inscription = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_numero_d_inscription.setObjectName("actionRecherche_par_numero_d_inscription")
        self.actionRecherche_pa_section = QtWidgets.QAction(MainWindow)
        self.actionRecherche_pa_section.setObjectName("actionRecherche_pa_section")
        self.actionRecherche_par_niveau = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_niveau.setObjectName("actionRecherche_par_niveau")
        self.actionRecherche_par_section_et_niveau = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_section_et_niveau.setObjectName("actionRecherche_par_section_et_niveau")
        self.actionAjouter_un_livre = QtWidgets.QAction(MainWindow)
        self.actionAjouter_un_livre.setObjectName("actionAjouter_un_livre")
        self.actionSupprimer_un_livre = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_un_livre.setObjectName("actionSupprimer_un_livre")
        self.actionModifier_un_livre = QtWidgets.QAction(MainWindow)
        self.actionModifier_un_livre.setObjectName("actionModifier_un_livre")
        self.actionAfficher_les_livres = QtWidgets.QAction(MainWindow)
        self.actionAfficher_les_livres.setObjectName("actionAfficher_les_livres")
        self.actionRechercher_par_r_f_rence = QtWidgets.QAction(MainWindow)
        self.actionRechercher_par_r_f_rence.setObjectName("actionRechercher_par_r_f_rence")
        self.actionRecherche_par_titre = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_titre.setObjectName("actionRecherche_par_titre")
        self.actionRecherche_par_auteur = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_auteur.setObjectName("actionRecherche_par_auteur")
        self.actionRecherche_par_ann_e = QtWidgets.QAction(MainWindow)
        self.actionRecherche_par_ann_e.setObjectName("actionRecherche_par_ann_e")
        self.actionAjouter_des_empruntes = QtWidgets.QAction(MainWindow)
        self.actionAjouter_des_empruntes.setObjectName("actionAjouter_des_empruntes")
        self.actionSupprimer_des_empruntes = QtWidgets.QAction(MainWindow)
        self.actionSupprimer_des_empruntes.setObjectName("actionSupprimer_des_empruntes")
        self.actionModifier_des_empruntes = QtWidgets.QAction(MainWindow)
        self.actionModifier_des_empruntes.setObjectName("actionModifier_des_empruntes")
        self.actionAfficher_emprunte = QtWidgets.QAction(MainWindow)
        self.actionAfficher_emprunte.setObjectName("actionAfficher_emprunte")
        self.actionRecherche_emprunte_par_date = QtWidgets.QAction(MainWindow)
        self.actionRecherche_emprunte_par_date.setObjectName("actionRecherche_emprunte_par_date")
        self.actionR_cup_ration = QtWidgets.QAction(MainWindow)
        self.actionR_cup_ration.setCheckable(False)
        self.actionR_cup_ration.setStatusTip("")
        self.actionR_cup_ration.setVisible(True)
        self.actionR_cup_ration.setShortcutVisibleInContextMenu(False)
        self.actionR_cup_ration.setObjectName("actionR_cup_ration")
        self.actionEnregistrement = QtWidgets.QAction(MainWindow)
        self.actionEnregistrement.setObjectName("actionEnregistrement")
        self.actionRechercher_tudiant = QtWidgets.QAction(MainWindow)
        self.actionRechercher_tudiant.setObjectName("actionRechercher_tudiant")
        self.actionRechercher_livre = QtWidgets.QAction(MainWindow)
        self.actionRechercher_livre.setObjectName("actionRechercher_livre")
        self.actionRetour_des_empruntes = QtWidgets.QAction(MainWindow)
        self.actionRetour_des_empruntes.setObjectName("actionRetour_des_empruntes")
        self.actionContenu_fichier_Etudiant = QtWidgets.QAction(MainWindow)
        self.actionContenu_fichier_Etudiant.setObjectName("actionContenu_fichier_Etudiant")
        self.actionContenu_fichier_Livre = QtWidgets.QAction(MainWindow)
        self.actionContenu_fichier_Livre.setObjectName("actionContenu_fichier_Livre")
        self.actionContenu_fichier_Emprunt = QtWidgets.QAction(MainWindow)
        self.actionContenu_fichier_Emprunt.setObjectName("actionContenu_fichier_Emprunt")
        self.actionEnonc_projet = QtWidgets.QAction(MainWindow)
        self.actionEnonc_projet.setObjectName("actionEnonc_projet")
        self.menuFile.addAction(self.actionAcceuil)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuMise_jour_des_tudiants.addAction(self.actionAjouter_un_tudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuMise_jour_des_tudiants.addAction(self.actionSupprimer_un_tudiant)
        self.menuMise_jour_des_tudiants.addSeparator()
        self.menuMise_jour_des_tudiants.addAction(self.actionModifier_un_tudiant)
        self.menuRecherche_et_affichage.addAction(self.actionAfficher_les_tudiants)
        self.menuRecherche_et_affichage.addSeparator()
        self.menuRecherche_et_affichage.addAction(self.actionRechercher_tudiant)
        self.menuRecherche_et_affichage.addSeparator()
        self.menuGestion_des_tudiants.addAction(self.menuMise_jour_des_tudiants.menuAction())
        self.menuGestion_des_tudiants.addSeparator()
        self.menuGestion_des_tudiants.addAction(self.menuRecherche_et_affichage.menuAction())
        self.menuMise_jour_des_livres.addAction(self.actionAjouter_un_livre)
        self.menuMise_jour_des_livres.addSeparator()
        self.menuMise_jour_des_livres.addAction(self.actionSupprimer_un_livre)
        self.menuMise_jour_des_livres.addSeparator()
        self.menuMise_jour_des_livres.addAction(self.actionModifier_un_livre)
        self.menuRecherche_et_affichage_2.addAction(self.actionAfficher_les_livres)
        self.menuRecherche_et_affichage_2.addSeparator()
        self.menuRecherche_et_affichage_2.addAction(self.actionRechercher_livre)
        self.menuGestion_des_Livres.addAction(self.menuMise_jour_des_livres.menuAction())
        self.menuGestion_des_Livres.addSeparator()
        self.menuGestion_des_Livres.addAction(self.menuRecherche_et_affichage_2.menuAction())
        self.menuMise_jour_des_empruntes.addAction(self.actionAjouter_des_empruntes)
        self.menuMise_jour_des_empruntes.addSeparator()
        self.menuMise_jour_des_empruntes.addAction(self.actionRetour_des_empruntes)
        self.menuMise_jour_des_empruntes.addSeparator()
        self.menuMise_jour_des_empruntes.addAction(self.actionSupprimer_des_empruntes)
        self.menuMise_jour_des_empruntes.addSeparator()
        self.menuMise_jour_des_empruntes.addAction(self.actionModifier_des_empruntes)
        self.menuRecherche_et_affichage_3.addAction(self.actionAfficher_emprunte)
        self.menuRecherche_et_affichage_3.addSeparator()
        self.menuRecherche_et_affichage_3.addAction(self.actionRecherche_emprunte_par_date)
        self.menuGestion_des_emprunts.addAction(self.menuMise_jour_des_empruntes.menuAction())
        self.menuGestion_des_emprunts.addSeparator()
        self.menuGestion_des_emprunts.addAction(self.menuRecherche_et_affichage_3.menuAction())
        self.menuEnregistrement_et_r_cup_ration.addAction(self.actionR_cup_ration)
        self.menuEnregistrement_et_r_cup_ration.addSeparator()
        self.menuEnregistrement_et_r_cup_ration.addAction(self.actionEnregistrement)
        self.menuEnregistrement_et_r_cup_ration.addSeparator()
        self.menuEnregistrement_et_r_cup_ration.addAction(self.actionEnonc_projet)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGestion_des_tudiants.menuAction())
        self.menubar.addAction(self.menuGestion_des_Livres.menuAction())
        self.menubar.addAction(self.menuGestion_des_emprunts.menuAction())
        self.menubar.addAction(self.menuEnregistrement_et_r_cup_ration.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuGestion_des_tudiants.setTitle(_translate("MainWindow", "Gestion des étudiants"))
        self.menuMise_jour_des_tudiants.setTitle(_translate("MainWindow", "Mise à jour des étudiants"))
        self.menuRecherche_et_affichage.setTitle(_translate("MainWindow", "Recherche et affichage"))
        self.menuGestion_des_Livres.setTitle(_translate("MainWindow", "Gestion des Livres"))
        self.menuMise_jour_des_livres.setTitle(_translate("MainWindow", "Mise à jour des livres"))
        self.menuRecherche_et_affichage_2.setTitle(_translate("MainWindow", "Recherche et affichage"))
        self.menuGestion_des_emprunts.setTitle(_translate("MainWindow", "Gestion des empruntes"))
        self.menuMise_jour_des_empruntes.setTitle(_translate("MainWindow", "Mise à jour des empruntes"))
        self.menuRecherche_et_affichage_3.setTitle(_translate("MainWindow", "Recherche et affichage"))
        self.menuEnregistrement_et_r_cup_ration.setTitle(_translate("MainWindow", "Enregistrement et récupération"))
        self.actionAcceuil.setText(_translate("MainWindow", "Acceuil"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAjouter_un_tudiant.setText(_translate("MainWindow", "Ajouter un étudiant"))
        self.actionSupprimer_un_tudiant.setText(_translate("MainWindow", "Supprimer un étudiant"))
        self.actionModifier_un_tudiant.setText(_translate("MainWindow", "Modifier un étudiant"))
        self.actionAfficher_les_tudiants.setText(_translate("MainWindow", "Afficher les étudiants"))
        self.actionRecherche_par_numero_d_inscription.setText(_translate("MainWindow", "Recherche par numero d\'inscription"))
        self.actionRecherche_pa_section.setText(_translate("MainWindow", "Recherche pa section"))
        self.actionRecherche_par_niveau.setText(_translate("MainWindow", "Recherche par niveau"))
        self.actionRecherche_par_section_et_niveau.setText(_translate("MainWindow", "Recherche par section et niveau"))
        self.actionAjouter_un_livre.setText(_translate("MainWindow", "Ajouter un livre"))
        self.actionSupprimer_un_livre.setText(_translate("MainWindow", "Supprimer un livre"))
        self.actionModifier_un_livre.setText(_translate("MainWindow", "Modifier un livre"))
        self.actionAfficher_les_livres.setText(_translate("MainWindow", "Afficher les livres"))
        self.actionRechercher_par_r_f_rence.setText(_translate("MainWindow", "Rechercher par référence"))
        self.actionRecherche_par_titre.setText(_translate("MainWindow", "Recherche par titre"))
        self.actionRecherche_par_auteur.setText(_translate("MainWindow", "Recherche par auteur"))
        self.actionRecherche_par_ann_e.setText(_translate("MainWindow", "Recherche par année"))
        self.actionAjouter_des_empruntes.setText(_translate("MainWindow", "Ajouter des emprunts"))
        self.actionSupprimer_des_empruntes.setText(_translate("MainWindow", "Supprimer des emprunts"))
        self.actionModifier_des_empruntes.setText(_translate("MainWindow", "Modifier des emprunts"))
        self.actionAfficher_emprunte.setText(_translate("MainWindow", "Afficher emprunts"))
        self.actionRecherche_emprunte_par_date.setText(_translate("MainWindow", "Recherche emprunts"))
        self.actionR_cup_ration.setText(_translate("MainWindow", "Récupération "))
        self.actionEnregistrement.setText(_translate("MainWindow", "Enregistrement"))
        self.actionRechercher_tudiant.setText(_translate("MainWindow", "Rechercher étudiant"))
        self.actionRechercher_livre.setText(_translate("MainWindow", "Rechercher livre"))
        self.actionRetour_des_empruntes.setText(_translate("MainWindow", "Retour des emprunts"))
        self.actionContenu_fichier_Etudiant.setText(_translate("MainWindow", "Contenu fichier Etudiant"))
        self.actionContenu_fichier_Livre.setText(_translate("MainWindow", "Contenu fichier Livre"))
        self.actionContenu_fichier_Emprunt.setText(_translate("MainWindow", "Contenu fichier Emprunt"))
        self.actionEnonc_projet.setText(_translate("MainWindow", "Enoncé projet"))