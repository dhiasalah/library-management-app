class Etudiant:
    def __init__(self, numero_inscription, nom, prenom, date_naissance, adresse, mail, tel, section, niveau_etude) -> None:
        self.numero_inscription = numero_inscription
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.mail = mail
        self.tel = tel
        self.section = section
        self.niveau_etude = niveau_etude

    def __str__(self):
        return "numero_inscription:" + self.numero_inscription + " nom:" + self.nom + "prenom: " + self.prenom