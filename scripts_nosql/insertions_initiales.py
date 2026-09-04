import json 
import pymongo
from scripts_nosql import helpers


def insert_all_documents(database):
    # Insertion de la liste des auteurs
    url_auteurs = 'donnees_initiales/auteurs.json'
    helpers.insertion_multiple(database,"Auteurs",url_auteurs)

    # Insertion de la liste des utilsateurs
    url_utilisateurs = 'donnees_initiales/utilisateurs.json'
    helpers.insertion_multiple(database,"Utilisateurs",url_utilisateurs)

    # Insertion de la liste des Livres
    url_livres = 'donnees_initiales/livres.json'
    helpers.enregistrer_livres(database,"Livres",url_livres)

    # Insertion de la liste des Emprunts
    url_emprunts = 'donnees_initiales/emprunts.json'
    helpers.enregistrer_emprunts(database,"Emprunts",url_emprunts)


def mis_a_jour_disponibilite_livre(database,isbn, statut):
    
    try:
        livre = database["Livres"].find_one({"isbn": isbn})
        livre["disponible"]= statut
        print(f"Le statut du livre {isbn} a été changé avec succès.")
    except :
        print("Impossible de changer le statut du livre. Veuillez réessayer.")

