from voiture import Voiture
from crud_db import connecter_db, ajouter_voiture,supprimer_voiture,recuperer_voitures

try:
    connexion = connecter_db()
    print("Connexion à la base de données réussie")
    connexion.close()
    print("Connexion fermée")
except Exception as e:
    print("Erreur de connexion :", e)
v1 = Voiture("Toyota", "Prius", 2020, 18500)
v2 = Voiture("Honda", "Civic", 2019, 17200)
v3 = Voiture("Audi", "A3", 2018, 24500)

ajouter_voiture(v1)
ajouter_voiture(v2)
ajouter_voiture(v3)
print("Voitures après ajout :")
voitures = recuperer_voitures()
for v in voitures:
    v.afficher_voiture()
supprimer_voiture(1)
print("Voiture supprimée avec succès")

print("Voitures après suppression :")
v.afficher_voiture()
voitures = recuperer_voitures()
print("Voitures après récupération :")
for v in voitures:
    v.afficher_voiture()