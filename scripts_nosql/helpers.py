import json

def open_json_doc(url_documents):
    with open(url_documents, "r", encoding="utf-8") as f:
            documents = json.load(f)
    return documents

def insertion(database, nom_collection, document):
    try: 
        collection = database[nom_collection]
        resultat = collection.insert_one(document)
        print(f"Les données de la collection {collection} ont été insérées avec succès")
    except:
       print("Le document soumis n'a pas pu être insérée. Merci de réessayer")

def insertion_multiple(database, nom_collection, url_documents):
    documents = open_json_doc(url_documents)
    try:
        collection = database[nom_collection]
        resultat = collection.insert_many(documents)
        print(f"Les données de la collection {collection} ont été insérées avec succès")
    except:
           print("Les documents soumis n'ont pas pu être insérés. Merci de réessayer")


def creer_index(database, nom_collection, champs_index, unique=False):
    try:
        collection = database[nom_collection]
        index_name = collection.create_index(champs_index, unique=unique)
        print(f"L'index {index_name} a été créé avec succès")
    except:
        print("Erreur lors de la creation de l'index. Merci de réessayer")


def enregistrer_emprunts(database, nom_collection, url_documents):
    emprunts = open_json_doc(url_documents)

    for emprunt in emprunts:
        utilisateur = database["Utilisateurs"].find_one({"id_utilisateur": emprunt["id_utilisateur"]})
        livre = database["Livres"].find_one({"isbn": emprunt["isbn"]})

        if not utilisateur:
            raise ValueError(f"L'utilisatreur {emprunt["id_utilisateur"]} est introuvable dans la base de données.")
        if not livre:
            raise ValueError(f"le livre {emprunt["isbn"]} est introuvable dans la base de données.")
        if livre.get("disponible", 0) == False:
            raise ValueError(f"Le livre {emprunt["isbn"]} demandé n'est pas disponible en stock ")

        
        nouvel_emprunt = {
            "id_utilisateur": emprunt["id_utilisateur"],
            "nom_utilisateur_copie": utilisateur["nom_utilisateur"],
            "isbn": emprunt["isbn"],
            "titre_livre_copie": livre["titre"],
            "date_emprunt": emprunt["date_emprunt"],
            "date_retour_prevue": emprunt["date_retour_prevue"],
            "date_retour_effective": emprunt["date_retour_effective"]
        }

        resultat = database[nom_collection].insert_one(nouvel_emprunt)
        print(f"L'emprunt pour l'utilisateur {emprunt["id_utilisateur"]} a été enregistré avec succès. Date de retour prévue : {emprunt["date_retour_prevue"]}.")

def enregistrer_livres(database, nom_collection, url_documents):

    livres = open_json_doc(url_documents)

    for livre in livres:
        auteurs_copies = []
        for id_auteur in livre["ids_auteurs"]:
            auteur = database["Auteurs"].find_one({"id_auteur": id_auteur})
            
            if not auteur:
                raise ValueError(f"L'auteur {id_auteur} est introuvable; Impossible de créer le livre")
            
            # Étape 2 — extraire uniquement le champ à copier (le nom)
            auteurs_copies.append({
                "id_auteur": id_auteur,
                "Nom_auteur_copie": auteur["nom"]
            })

        
        nouveau_livre = {
            "isbn": livre["isbn"],
            "titre": livre["titre"],
            "auteurs": auteurs_copies,
            "date": livre["date"],
            "tags": livre["tags"],
            "resume": livre["resume"],
            "disponible": True
        }

        resultat = database[nom_collection].insert_one(nouveau_livre)
        print(f"Le livre avec ISBN {livre["isbn"]} est créé avec succès.")