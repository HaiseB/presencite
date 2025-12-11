# 📅 Presencite – Gestion de présence avec émojis 🧑‍💼✅❌

**Presencité** est une application web développée avec **Django** qui permet aux utilisateurs d'indiquer leur présence sur site pour chaque jour de la semaine, en utilisant un système simple et ludique d’émojis.

## ✨ Fonctionnalités principales

- ✅🧑‍💼 Chaque utilisateur peut déclarer sa présence ou son absence pour chaque jour de la semaine
- 🧑‍🤝‍🧑 Les utilisateurs peuvent voir ce que les autres ont rempli
- 🔒 Une fois validée, une semaine n’est plus modifiable
- 🕵️‍♂️ Un admin peut consulter :
  - les semaines précédentes
  - qui n’a pas rempli ses jours

### 🔁 Émojis utilisés

- **Présent** : ✅ `:coche_blanche:` ou 🏢 `:bureau:`
- **Absent** : ❌ `:x:`, 🎓 `:école:`, 🌴 `:palmier:`, 👮 `:policier:`

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-utilisateur/presencite.git
cd presencite
```

### 2. Créer et activer un environnement virtuel
```bash
python -m venv venv
```
Windows :
```bash
venv\Scripts\activate
```
macOS/Linux :

```bash
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Créer un superutilisateur (optionnel, pour l'admin)
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement
```bash
python manage.py runserver 0.0.0.0:8000
```

## 🚀 Utilisation
Accès au site : http://127.0.0.1:8000

Accès à l’interface d’administration : http://127.0.0.1:8000/admin

## 🔧 Stack technique
- Python 3.10+
- Django 4.2+
- SQLite (par défaut, peut être remplacée par PostgreSQL)
- HTML/CSS minimaliste (possibilité de styliser avec Tailwind ou Bootstrap)

## 📄 Licence
Ce projet est open-source sous licence MIT.
