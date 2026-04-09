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