## 🎯 **Nom du Projet : TaskFlow - Gestionnaire de Tâches Collaboratif**

### **Description générale :**

Créer une application en ligne de commande (CLI) puis, si possible, avec une interface graphique basique, qui permet de
gérer des tâches (ajout, suppression, modification, marquage comme terminées) pour un ou plusieurs utilisateurs.

Tu peux pousser le projet plus loin en intégrant des fonctionnalités collaboratives et en explorant des concepts avancés
comme la persistance des données, les bases de données ou l'API REST.

---

### 📆 **Plan en 3 Semaines :**

#### **Semaine 1 : Fonctionnalités de Base**

#### Objectif : Construire un gestionnaire de tâches en ligne de commande

- Ajouter une tâche :
    - Demander à l'utilisateur une description claire de la tâche.
    - Permettre de choisir une priorité parmi : basse, normale, haute.
    - Ajouter une date limite au format (exemple : JJ/MM/AAAA).
    - Attribuer un statut initial (par défaut "en cours").
- Lister les tâches existantes avec des options de filtres :
    - Par statut (en cours, terminée, supprimée).
    - Par priorité (basse, normale, haute).
    - Par date limite (triées par ordre croissant).
- Supprimer une tâche (changer son statut à "supprimée" plutôt que de l'effacer complètement).
- Modifier une tâche existante :
    - Modifier la description, la priorité, ou la date limite.

#### Structure du code suggérée :

- Créer une classe `Task` avec les attributs suivants :
    - `description`
    - `priority`
    - `due_date`
    - `status`
- Créer une classe `TaskManager` qui contiendra :
    - Une liste de tâches.
    - Des méthodes pour ajouter, supprimer, modifier, et lister les tâches.

#### Exemple de structure pour les données :

```json
{
  "tasks": [
    {
      "description": "Préparer la réunion",
      "priority": "haute",
      "due_date": "20/12/2024",
      "status": "en cours"
    },
    {
      "description": "Acheter des fournitures",
      "priority": "normale",
      "due_date": "25/12/2024",
      "status": "terminée"
    }
  ]
}
```

#### Gestion des entrées utilisateur :

- Construire un menu interactif en ligne de commande avec des options :
    - Ajouter une tâche.
    - Modifier une tâche.
    - Supprimer une tâche.
    - Lister les tâches (avec filtres).
    - Quitter.

- Utiliser des boucles et des conditions pour maintenir le programme en fonctionnement jusqu'à ce que l'utilisateur
  choisisse de quitter.

#### Compétences visées :

* Programmation orientée objet (OOP), évaluée par la capacité à créer et manipuler des classes comme Task et TaskManager
  pour structurer le code.
* Manipulation des listes, dictionnaires et fichiers (json, csv), mesurée par la capacité à sauvegarder et charger
  les
  données des tâches tout en maintenant leur intégrité.
* Gestion des entrées utilisateurs avec des menus interactifs, validée par l'implémentation d'un menu robuste et
  intuitif
  pour ajouter, modifier, et afficher les tâches.

* Améliorations possibles :
    * Sauvegarder les données dans un fichier JSON pour persister les tâches entre les exécutions.

    * Charger les données existantes depuis le fichier au démarrage du programme.

#### **Semaine 2 : Collaboration et Persistance Avancée**

1. **Objectif : Ajouter une gestion multi-utilisateur avec des bases de données simples.**
    - Chaque utilisateur a ses propres tâches.
    - Implémenter un système d'authentification simple (nom d'utilisateur et mot de passe).
    - Utiliser **SQLite** pour stocker les tâches et les utilisateurs.

2. **Compétences visées :**
    - Utilisation d'une base de données SQLite avec la librairie `sqlite3`.
    - Structuration du code pour séparer la logique (MVC : Modèle, Vue, Contrôleur basique).
    - Gestion d'erreurs et validation des données.

3. **Améliorations possibles :**
    - Ajouter des rappels de tâches (envoie un message à la console si une tâche est proche de la date limite).

---

#### **Semaine 3 : Interface Graphique et Collaboration**

1. **Objectif : Créer une interface utilisateur simple et connecter le projet à une API locale.**
    - Utiliser **Tkinter** pour concevoir une interface graphique.
    - Afficher les tâches dans une liste déroulante avec des boutons pour ajouter, modifier et supprimer.
    - Implémenter une API REST (avec **Flask**) pour rendre les données accessibles.

2. **Compétences visées :**
    - Création d'une interface graphique avec Tkinter.
    - Développement d'une API RESTful avec Flask.
    - Communication entre un client (interface graphique) et une API.

3. **Améliorations possibles :**
    - Ajouter une synchronisation des tâches en temps réel (par exemple, via des fichiers partagés ou une API en ligne).
    - Exporter les tâches en PDF ou en Excel.

---

### 🛠 **Technologies et Outils suggérés :**

- **Langage :** Python
- **Base de données :** SQLite (ou JSON pour commencer)
- **Framework Web/API :** Flask
- **Interface graphique :** Tkinter
- **Librairies :** `sqlite3`, `flask`, `tkinter`, `json`, `csv`, `reportlab` (pour l'export PDF).

---

### 🚀 **Livrables finaux :**

- Une application fonctionnelle avec :
    - Gestion complète des tâches.
    - Support multi-utilisateur.
    - Interface graphique simple.
    - Documentation claire (README).
- Un fichier de base de données SQLite ou JSON.
- Optionnel : un export PDF des tâches.

---

### 🧠 **Pourquoi ce projet ?**

Ce projet te permettra de travailler sur :

- **Programmation Orientée Objet (POO)**.
- **Bases de données et persistance des données**.
- **Interfaces graphiques**.
- **Développement d'une API REST**.
- **Gestion de projet et organisation du code**.

---
