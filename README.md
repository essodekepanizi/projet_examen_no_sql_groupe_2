

# Téléchargement des dossiers du projet
Ouvrir le repertoire github du projet via le lien suivant:
[Lien Repertoire Github Du projet](https://github.com/essodekepanizi/projet_examen_no_sql_groupe_2)
Télécharger le projet en fichier zip depuis github

Décompresser le fichier zip dans le dossier de votre choix.

# Installation des packages et drivers nécessaires

Ouvrir le terminal de votre ordinateur (Powershell sur Windows / Terminal sur Mac)
Naviguer dans le dossier décompressé ou se trouve le code python principal 'gestion_de_bibliothèques_avec_nosql_groupe_2.py'

Lancer la commande bash d'installation des packages et drivers requis

`pip install -r requirements.txt`

# Configuration des accès à la base de données MongoDB Atlas

Créer un fichier `.env` dans le même dossier que le script principal `main.py`
Ajouter la variable du lien vers la base de données suivante dans le fichier .env crée  :
Le lien exacte est envoyé dans un canal séparé via la plateforme du cours ESMT.

MONGODB_URI="xxxxxxx" 

# Exécution du script 
Lancer la commande bash suivante pour exécuter le programme:

`python main.py`

