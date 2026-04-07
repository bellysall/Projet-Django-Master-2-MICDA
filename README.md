 
# Projet Blog Django - Master 2 MICDA

## Description

Ce projet est une application web développée avec Django dans le cadre de l'examen de Langages et Frameworks Backend 2.

Il s'agit d'un blog complet permettant :

* l'affichage des articles
* la lecture détaillée d'un article
* la création d'articles
* la modification d'articles
* la suppression d'articles

Le projet utilise les Class Based Views (CBV).

## Fonctionnalités réalisées

* ListView : liste des articles
* DetailView : détail d’un article
* CreateView : ajout d’un article
* UpdateView : modification d’un article
* DeleteView : suppression d’un article

## Administration Django

* Modèle Article enregistré dans l’administration
* Gestion des images
* Gestion auteur et date de publication

## Technologies utilisées

* Python
* Django
* SQLite
* HTML
* CSS

## Installation

### 1. Cloner le projet

git clone lien_du_depot

### 2. Aller dans le dossier

cd monprojet

### 3. Créer environnement virtuel

python -m venv env

### 4. Activer environnement

env\Scripts\activate

### 5. Installer Django

pip install django pillow

### 6. Lancer migrations

python manage.py makemigrations
python manage.py migrate

### 7. Créer administrateur

python manage.py createsuperuser

### 8. Lancer serveur

python manage.py runserver

## pour Ouvrir le navigateur
http://127.0.0.1:8000/

## pour Admin Django
http://127.0.0.1:8000/admin/

## Auteur

Projet réalisé par Faty Belly SALL (fatybelly.sall@unchk.edu.sn) Master 2 MICDA
