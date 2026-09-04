
def nombre_livres_par_auteur(db):
    pipeline = [
        {"$unwind": "$auteurs"},
        {
            "$group": {
            "_id": "$auteurs.id_auteur",
            "nom_auteur": { "$first": "$auteurs.Nom_auteur_copie" },
            "nombre_livres": { "$sum": 1 }
            }
        },
        { "$sort": {"nombre_livres": -1 } }
    ]

    for r in db["Livres"].aggregate(pipeline):
        print(f"{r['nom_auteur']} : {r['nombre_livres']} livre(s)")



def liste_livres_emprunts_encours(database):

    emprunts_encours = database["Emprunts"].find({"date_retour_effective": None})

    liste_isbn = set()

    for emprunt in emprunts_encours:
        liste_isbn.add(emprunt["isbn"])

   
    print("La liste des livres empruntés et pas encore retournés est composée de : ")
    for isbn in liste_isbn:
        livre = database["Livres"].find_one({"isbn": isbn})
        print(livre["titre"])