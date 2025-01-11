# Projet de Gestion Bancaire

Ce projet est une application de gestion bancaire en ligne qui permet aux utilisateurs de créer des comptes, de gérer leurs soldes, de mettre à jour leurs informations personnelles, et de réaliser des opérations bancaires de base comme le crédit et le débit. Il inclut également un panneau d'administration pour gérer les comptes utilisateurs.

## Fonctionnalités

### Pour les Utilisateurs
- **Inscription** : Créer un nouveau compte bancaire avec un nom d'utilisateur, un mot de passe, un email, un numéro de téléphone et un solde initial.
- **Connexion** : Authentification sécurisée avec un nom d'utilisateur et un mot de passe.
- **Gestion du Solde** :
  - Créditer le compte.
  - Débiter le compte.
  - Afficher le solde actuel.
- **Mise à Jour des Informations** : Modifier le nom d'utilisateur, l'email ou le numéro de téléphone.
- **Affichage des Détails du Compte** : Voir toutes les informations personnelles et le solde du compte.
- **Suppression de Compte** : Supprimer un compte utilisateur.

### Pour l'Administrateur
- **Suppression de Comptes** :
  - Supprimer un compte unique.
  - Supprimer plusieurs comptes en une seule opération.
- **Visualisation des Comptes** : Afficher tous les comptes existants avec leurs détails.

## Technologies Utilisées

- **Python** : Langage de programmation principal.
- **JSON** : Stockage des données utilisateur dans un fichier `users.txt`.
- **Modules Python** :
  - `os` : Pour effacer l'écran et gérer les fichiers.
  - `sys` : Pour quitter le programme.
  - `time` : Pour ajouter des délais dans l'affichage.
  - `json` : Pour lire et écrire des données au format JSON.
  - `getpass` : Pour masquer le mot de passe lors de la saisie.

## Structure du Projet

- **Fichier Principal** : `main.py` (ou le nom de votre fichier Python).
- **Fichier de Données** : `users.txt` (stocke les informations des utilisateurs au format JSON).
- **Fonctions Principales** :
  - `signup()` : Gère l'inscription des utilisateurs.
  - `login()` : Gère l'authentification des utilisateurs.
  - `submenu()` : Menu des opérations bancaires après connexion.
  - `admin()` : Panneau d'administration pour gérer les comptes.
  - `remove_single_account()` : Supprime un compte unique.
  - `remove_multiple_accounts()` : Supprime plusieurs comptes.
  - `view_all_accounts()` : Affiche tous les comptes existants.

## Comment Utiliser

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git