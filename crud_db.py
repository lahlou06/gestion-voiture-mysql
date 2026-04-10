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