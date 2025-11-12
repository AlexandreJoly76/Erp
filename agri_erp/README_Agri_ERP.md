# 🌾 Agri ERP — Mini ERP Django

## 📘 Présentation

**Agri ERP** est un mini système ERP développé avec **Django (Python)**.  
Ce projet illustre la gestion des **produits, clients, commandes** et **lignes de commande**, avec calcul automatique des totaux HT/TTC et interface d'administration complète.

Ce projet a été conçu à des fins pédagogiques dans le cadre d'une préparation à un poste en alternance chez **Agorinfo**, une entreprise spécialisée dans les ERP.

---

## 🧩 Fonctionnalités principales

### 💼 Gestion des produits
- Création, modification, suppression de produits.
- Calcul automatique de la **valeur du stock** (`prix * quantité`).
- Indicateur d'alerte de stock faible (`en_alerte` avec seuil).

### 👥 Gestion des clients
- Type de client (professionnel / particulier).
- Informations de contact.
- Historique des commandes liées.

### 🧾 Gestion des commandes
- Création d'une commande via un **formulaire dynamique**.
- Ajout de plusieurs lignes de commande à la volée grâce à un **Inline Formset**.
- Calcul automatique du **total HT** et **total TTC**.

### 🧮 Administration Django
- Interface personnalisée avec filtres, recherches et colonnes calculées.
- **Inline editing** des lignes de commande dans l’admin.
- Tri par date, client ou statut.

---

## ⚙️ Architecture du projet

```
erp-training/
└─ agri_erp/
   ├─ manage.py
   ├─ agri_erp/
   │  ├─ settings.py
   │  ├─ urls.py
   │  └─ wsgi.py / asgi.py
   └─ stocks/
       ├─ models.py
       ├─ admin.py
       ├─ forms.py
       ├─ views.py
       ├─ urls.py
       └─ templates/stocks/
           ├─ product_list.html
           ├─ order_form.html
           └─ order_detail.html
```

---

## 🏗️ Installation

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/votre-profil/agri_erp.git
cd agri_erp
```

### 2️⃣ Créer un environnement virtuel
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Lancer l'environnement
```bash
cd erp-training
source .venv/bin/activate
```

### Lancer le serveur
```bash
cd agri_erp
python3 manage.py runserver
```

### 3️⃣ Installer les dépendances
```bash
pip install django
```

### 4️⃣ Appliquer les migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 6️⃣ Lancer le serveur
```bash
python manage.py runserver
```
Accéder à :
- 🧭 **http://127.0.0.1:8000/** → Application
- 🔐 **http://127.0.0.1:8000/admin/** → Interface d'administration

---

## 🧠 Points techniques à retenir

- Utilisation du **ORM Django** pour manipuler les données sans SQL brut.  
- **ModelForms** et **InlineFormset** pour créer des formulaires liés.
- **Propriétés Python** pour encapsuler la logique métier (`total_ht`, `valeur_stock`, etc.).
- **Admin Django** personnalisé pour une expérience utilisateur fluide.

---

## 🚀 Pistes d'amélioration

- Validation du stock disponible lors de la création d'une commande.
- Décrémentation automatique du stock après validation d'une commande.
- Importation des produits via un fichier CSV.
- Tableau de bord récapitulatif (chiffre d’affaires, clients, stocks).

---

## 👨‍💻 Auteur

**Zone01 Rouen — Projet de formation Django**  
Créé par un étudiant en formation **Concepteur Développeur d'Applications**  
dans le cadre d'une préparation à une alternance chez **Agorinfo**.

---

> Ce projet met en avant la compréhension de Django, de l’ORM et des concepts ERP essentiels.
