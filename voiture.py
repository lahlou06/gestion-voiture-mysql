class Voiture:
    def __init__(self, marque, modele, annee, prix, id=None):
        self.id = id
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def afficher_voiture(self):
        print(f"ID: {self.id} | Marque: {self.marque} | Modèle: {self.modele} | Année: {self.annee} | Prix: {self.prix}$")