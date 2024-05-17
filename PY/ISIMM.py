from playsound import playsound
from gtts import gTTS
class ISIMM:
    def __init__(self):
        self.etudiants=[]
        self.livres=[]
        self.empruntes=[]
        self.accounts=[]



    #gestion des comptes
    def ajouter_account(self,a):
        self.accounts.append(a)
    def rechercher_account_paradresse(self,adresse):
        for e in self.accounts:
            if (e.adresse == adresse):
                return e
        return None
    def rechercher_account_parmotpasse(self,mot_passe):
        for e in self.accounts:
            if(e.mot_passe==mot_passe):
                return e
        return None
    def recherche_account(self,adresse,mot_passe):
        for e in self.accounts:
            if(e.adresse==adresse and e.mot_passe==mot_passe):
                return e
        return None

    #gestion etudiant
    def ajouter_etudiant(self,e):
        self.etudiants.append(e)
    def recherche_etudiant(self,numero_inscription):
        for e in self.etudiants:
            if(e.numero_inscription==numero_inscription):
                return e
        return None

    def supprimer_etudiant(self,numero_inscription):
        e=self.recherche_etudiant(numero_inscription)
        if e:
            self.etudiants.remove(e)
    def supprimer_etudiant_section(self,section):
        self.etudiants=[e for e in self.etudiants if e.section!=section]

    def supprimer_etudiant_niveau(self,niveau):
        self.etudiants=[e for e in self.etudiants if e.niveau_etude!=niveau]
    def supprimer_etudiant_niveau_section(self,niveau,section):
        self.etudiants=[e for e in self.etudiants if e.niveau_etude!=niveau or e.section!=section]


    def modifier_etudiant(self,numero_inscription,adresse,mail,telephone):
        e=self.recherche_etudiant(numero_inscription)
        if e:
            e.adresse=adresse
            e.mail=mail
            e.tel=telephone


    #gestion livre
    def ajouter_livre(self,l):
        self.livres.append(l)

    def recherche_livre(self,reference):
        for l in self.livres:
            if (l.reference == reference):
                return l
        return None
    def recherche_livre_par_titre(self,titre):
        for l in self.livres:
            if (l.titre == titre):
                return l
        return None
    def supprimer_livre(self,reference):
        l=self.recherche_livre(reference)
        if l:
            self.livres.remove(l)

    def supprimer_livre_auteur(self, auteur):
        self.livres = [l for l in self.livres if l.nom_prenom_auteur != auteur]
    def supprimer_livre_annee(self,annee):
        self.livres=[l for l in self.livres if l.anne_edition!=annee]

    def modifier_livre(self,reference,nombre_exp):
        l=self.recherche_livre(reference)
        if l:
            l.nombre_exp=nombre_exp
    def recherche_livre_par_auteur(self,auteur):
        for l in self.livres:
            if (l.nom_prenom_auteur == auteur):
                return l
        return None
    def recherche_livre_par_annee(self,annee):
        for l in self.livres:
            if (l.anne_edition == annee):
                return l
        return None


    #gestion emprunt
    def ajouter_emprunt(self,e):
        self.empruntes.append(e)

    def recherche_emprunt(self,numero_inscription):
        for l in self.empruntes:
            if (l.numero_inscription == numero_inscription):
                return l
        return None
    def recherche_emprunt_par_ref(self,ref):
        for l in self.empruntes:
            if (l.reference ==ref):
                return l
        return None
    def recherche_emprunt_pour_supprimer(self,numero_inscription,reference):
        for e in self.empruntes:
            if (e.numero_inscription == numero_inscription and e.reference==reference):
                return e
        return None

    def retourner_emprunt(self,reference):
        l=self.recherche_livre(reference)
        if l:
            x=int(l.nombre_exp)
            x=x+1
            l.nombre_exp=str(x)
    def supprimer_emprunt(self,numero_inscription,reference):
        e = self.recherche_emprunt_pour_supprimer(numero_inscription,reference)
        if e:
            self.empruntes.remove(e)


    def modifier_emprunt(self, numero_inscription,date_emprunt,date_retour):
        e = self.recherche_emprunt(numero_inscription)
        if e:
            e.date_emprunt = date_emprunt
            e.date_retour = date_retour


