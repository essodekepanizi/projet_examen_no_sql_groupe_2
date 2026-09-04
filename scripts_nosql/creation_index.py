from scripts_nosql import helpers

def index_titre_livre(database):
    helpers.creer_index(database,"Livres",("titre"))

def index_compose(database,nom_collection,  champs):
    helpers.creer_index(database,nom_collection,champs)