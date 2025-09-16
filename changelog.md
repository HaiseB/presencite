# Changelog

## Version 1.3.0 - 2024-01-20

### ✨ Nouvelles fonctionnalités
- **Système de changelog interactif** : Modale élégante avec chargement dynamique du contenu Markdown
- **Modales d'options** : Interface modernisée pour les paramètres d'affichage
- **Modale de confirmation de déconnexion** : Protection contre les déconnexions accidentelles
- **Lien d'administration** : Accès rapide à l'interface d'administration Django pour les administrateurs
- **Logo cliquable** : Retour à l'accueil en un clic sur le logo Attineos
- **Interface d'administration personnalisée** : Gestion complète des présences, profils et messages

### 🎨 Améliorations de l'interface
- **Charte graphique unifiée** : Page de login intégrée au design Attineos
- **Modales cohérentes** : Style uniforme avec la classe `.modal-attineos`
- **Navigation améliorée** : Liens vers GitHub, changelog, administration
- **Responsive design** : Interface optimisée pour tous les écrans

### 🔧 Améliorations techniques
- **Code factorisé** : Styles CSS centralisés dans `attineos.css`
- **JavaScript moderne** : Gestion des modales et déconnexion sécurisée
- **Administration Django** : Interface complète avec filtres, recherche et édition rapide
- **Sécurité renforcée** : Déconnexion par POST avec token CSRF
- **Redirection automatique** : Retour au login après déconnexion

### 🐛 Corrections
- **Erreur HTTP 405** : Résolution du problème de déconnexion
- **Affichage des modales** : Correction des problèmes de visibilité du contenu
- **Navigation** : Liens fonctionnels et cohérents

---

## Version 1.2.0 - 2024-01-15

### ✨ Nouvelles fonctionnalités
- Ajout du système de changelog avec modale interactive
- Amélioration de l'interface utilisateur avec Bootstrap 5
- Nouvelle fonctionnalité de verrouillage des présences

### 🐛 Corrections
- Correction du bug d'affichage des emojis sur mobile
- Résolution du problème de synchronisation des données

### 🔧 Améliorations techniques
- Mise à jour des dépendances
- Optimisation des performances de la base de données

---

## Version 1.1.0 - 2024-01-01

### ✨ Nouvelles fonctionnalités
- Système de gestion des présences hebdomadaires
- Interface de tableau de bord intuitive
- Gestion des profils utilisateurs

### 🔧 Améliorations techniques
- Migration vers Django 5.2
- Amélioration de la sécurité des sessions

---

## Version 1.0.0 - 2023-12-15

### 🎉 Première version
- Lancement de l'application de gestion des présences
- Système d'authentification utilisateur
- Interface de base pour la saisie des présences
