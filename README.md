# Créez une API sécurisée RESTful en utilisant Django REST

Livrable du Projet 10 du parcours *"Developpeur d'Application Python d'OpenClassrooms"*

Developpement d'une application permettant de remonter et suivre des problèmes techniques (issue tracking system).

L'API Softdesk permet aux utilisateurs de créer des projets, d'ajouter des contributeurs aux projets, de créer des problèmes et des commentaires.

Pour plus de détails sur le fonctionnement de cette API, se référer à cette [documentation](lien_vers_documentation) (Postman).

## Pré-requis
    - Python >= 3.11.1
    - Pip >= 22.3.1
    - Postman >= 10.11.1

## Installation (Windows)

Ouvrir une invite de commande (terminal) et se rendre dans le dossier souhaité pour l'installation de l'application (avec la commande `cd nom_du_dossier`), ensuite exécuter les commandes suivantes : 

1. Cloner le "repository" sur votre ordinateur
```shell
git clone https://github.com/iuliancojocari/sofdesk.git
```

2. Naviquer dans le dossier de l'application que vous venez de cloner
```shell
cd softdesk
```

3. Créer un environnement virtuel Python
```shell
python -m venv venv
```

4. Activer l'environnement virtuel Python
```shell
./venv/scripts/activate
```

5. Installer les paquets nécessaires au bon fonctionnement de l'application
```shell
pip install -r requirements.txt
```

## Utilisation

Lancer le serveur Django avec la commande:
```shell
python manage.py runserver
```

Pour naviguer dans l'API vous pouvez utiliser différents outils, comme : 
- Postman (https://www.postman.com/)
- via l'interface Django Rest Framework via l'adresse http://127.0.0.1:8000 (cf. points de terminaison ci-dessous)

## Informations

#### Liste des utilisateurs existants :

| *ID* | *Identifiant* | *Mot de passe* |
|------|---------------|----------------|
| 1    | utilisateur_1 |   Azerty1234   |
| 2    | utilisateur_2 |   Azerty1234   |
| 3    | utilisateur_3 |   Azerty1234   |

#### Liste des points de terminaison de l'API ([documentation](lien_postman_documentation)) :

| #   | *Point de terminaison d'API*                                              | *Méthode HTTP* | *URL (par défaut: http://127.0.0.1:8000)*       |
|-----|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| 1   | Inscription de l'utilisateur                                              | POST           | /signup/                                  |
| 2   | Connexion de l'utilisateur                                                | POST           | /login/                                   |
| 3   | Récupérer la liste de tous les projets rattachés à l'utilisateur connecté | GET            | /projects/                                |
| 4   | Créer un projet                                                           | POST           | /projects/                                |
| 5   | Récupérer les détails d'un projet via son id                              | GET            | /projects/{id}/                           |
| 6   | Mettre à jour un projet                                                   | PUT            | /projects/{id}/                           |
| 7   | Supprimer un projet et ses problèmes                                      | DELETE         | /projects/{id}/                           |
| 8   | Ajouter un utilisateur (collaborateur) à un projet                        | POST           | /projects/{id}/users/                     |
| 9   | Récupérer la liste de tous les utilisateurs attachés à un projet          | GET            | /projects/{id}/users/                     |
| 10  | Supprimer un utilisateur d'un projet                                      | DELETE         | /projects/{id}/users/{id}/                |
| 11  | Récupérer la liste des problèmes liés à un projet                         | GET            | /projects/{id}/issues/                    |
| 12  | Créer un problème dans un projet                                          | POST           | /projects/{id}/issues/                    |
| 13  | Mettre à jour un problème dans un projet                                  | PUT            | /projects/{id}/issues/{id}/               |
| 14  | Supprimer un problème d'un projet                                         | DELETE         | /projects/{id}/issues/{id}/               |
| 15  | Créer des commentaires sur un problème                                    | POST           | /projects/{id}/issues/{id}/comments/      |
| 16  | Récupérer la liste de tous les commentaires liés à un problème            | GET            | /projects/{id}/issues/{id}/comments/      |
| 17  | Modifier un commentaire                                                   | PUT            | /projects/{id}/issues/{id}/comments/{id}/ |
| 18  | Supprimer un commentaire                                                  | DELETE         | /projects/{id}/issues/{id}/comments/{id}/ |
| 19  | Récupérer un commentaire via son id                                       | GET            | /projects/{id}/issues/{id}/comments/{id}/ |