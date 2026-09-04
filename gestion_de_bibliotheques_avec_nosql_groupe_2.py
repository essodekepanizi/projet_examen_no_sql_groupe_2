
"""# Importation des bibliothèques nécessaires"""
import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv
from scripts_nosql import insertions_initiales, aggregations_de_donnees, creation_index

dotenv_path = Path(__file__).resolve().parent / ".env"

load_dotenv(dotenv_path=dotenv_path)

"""# Creation et accès à la base de données MongoDB"""

MONGO_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGO_URI)

nom_db = "bibliotheque_numerique"

# Supprimer la base de données si elle existe déjà
if nom_db in client.list_database_names():
    client.drop_database(nom_db)
    print(f"La base de données '{nom_db}' existait déjà et a été supprimée.")
else:
    print(f"La base de données '{nom_db}' n'existait pas encore.")

db = client[nom_db]

"""# Creation des collections"""
collections = ["Auteurs","Livres", "Utilisateurs","Emprunts"]

for collection in collections:
    if collection not in db.list_collection_names():
        db.create_collection(collection)
        print(f"La collection {collection} a été créée avec succès.")
    else:
        print(f"La collection {collection} existe déjà.")

print("*******"*10)
"""# Operations CRUD (Insertion de documents dans les collections)"""
# Insertions des documents (Livres, auteurs, emprunts, utilisateurs)
insertions_initiales.insert_all_documents(db)

print("*******"*10)
# Mise à jour d'un livre avec le statut de disponibilité = False
isbn = '978-2-07-036002-4'
insertions_initiales.mis_a_jour_disponibilite_livre(db, isbn, False)

print("*******"*10)

"""# Creation des Indexes utiles"""
creation_index.index_titre_livre(db)

champs_a_indexer = [
    ("id_utilisateur", 1),
    ("date_retour_effective", 1),
    ("date_emprunt", -1)
]

# Creation index composé pour optimiser une requête sur la collection emprunts
creation_index.index_compose(db,"Emprunts",champs_a_indexer)

# Extraction de données par requêtage

print("*******"*10)

aggregations_de_donnees.nombre_livres_par_auteur(db)


print("*******"*10)

aggregations_de_donnees.liste_livres_emprunts_encours(db)