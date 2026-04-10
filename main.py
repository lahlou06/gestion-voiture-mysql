from crud_db import connecter_db

try:
    connexion = connecter_db()
    print("Connexion à la base de données réussie")
    connexion.close()
    print("Connexion fermée")
except Exception as e:
    print("Erreur de connexion :", e)
