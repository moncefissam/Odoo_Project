# Gestion des Annonces (Odoo Module)

## Description
**Gestion des Annonces** est un module Odoo pour la gestion des annonces internes.

**Auteur:** ISSAM MOUNSSIF  
**Version:** 1.0  
**Dépendances:** base

## Technologies
- **Odoo:** 17.0
- **PostgreSQL:** 16

## Installation et Démarrage

Ce projet utilise Docker Compose pour orchestrer l'environnement.

1.  **Cloner le dépôt** (ou naviguer vers le dossier du projet).
2.  **Démarrer les conteneurs :**
    ```bash
    docker-compose up -d
    ```

## Accès

- **Interface Web Odoo :** [http://localhost:8069](http://localhost:8069)
- **Base de données :** `odoo_db`

## Configuration Base de Données (Docker)

Les informations d'identification de la base de données configurées dans `docker-compose.yml` sont :

- **Utilisateur :** `odoo`
- **Mot de passe :** `odoo`
