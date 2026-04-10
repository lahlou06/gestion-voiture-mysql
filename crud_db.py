import mysql.connector
import json

def connecter_db():
    with open("config.json") as f:
        config = json.load(f)

    connexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    return connexion
def ajouter_voiture(voiture):
    connexion = connecter_db()
    curseur = connexion.cursor()

    curseur.execute('\n'
                    '        CREATE TABLE IF NOT EXISTS voiture (\n'
                    '            id INT AUTO_INCREMENT PRIMARY KEY,\n'
                    '            marque VARCHAR(50),\n'
                    '            modele VARCHAR(50),\n'
                    '            annee INT,\n'
                    '            prix DECIMAL(10,2)\n'
                    '        )\n'
                    '    ')

    requete = """
        INSERT INTO voiture (marque, modele, annee, prix)
        VALUES (%s, %s, %s, %s)
    """
    valeurs = (voiture.marque, voiture.modele, voiture.annee, voiture.prix)

    curseur.execute(requete, valeurs)
    connexion.commit()

    curseur.close()
    connexion.close()

def supprimer_voiture(id):
    connexion = connecter_db()
    curseur = connexion.cursor()

    requete = "DELETE FROM voiture WHERE id = %s"
    curseur.execute(requete, (id,))
    connexion.commit()

    curseur.close()
    connexion.close()
from voiture import Voiture

def recuperer_voitures():
        connexion = connecter_db()
        curseur = connexion.cursor()

        requete = "SELECT id, marque, modele, annee, prix FROM voiture"
        curseur.execute(requete)

        resultats = curseur.fetchall()
        voitures = []

        for ligne in resultats:
            voiture = Voiture(
                ligne[1],
                ligne[2],
                ligne[3],
                ligne[4],
                ligne[0]
            )
            voitures.append(voiture)

        curseur.close()
        connexion.close()

        return voitures

def modifier_voiture(voiture):
    connexion = connecter_db()
    curseur = connexion.cursor()

    requete = """
    UPDATE voiture
    SET marque = %s, modele = %s, annee = %s, prix = %s
    WHERE id = %s
    """

    valeurs = (
        voiture.marque,
        voiture.modele,
        voiture.annee,
        voiture.prix,
        voiture.id
    )

    curseur.execute(requete, valeurs)
    connexion.commit()

    curseur.close()
    connexion.close()