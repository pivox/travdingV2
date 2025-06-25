# 📊 Trading Kline API

Une API légère basée sur **FastAPI** permettant de charger et analyser les données Kline pour une paire de trading et un intervalle donné.

---

## 🚀 Démarrage rapide

### 🔧 Prérequis

- Python 3.11+
- Docker & Docker Compose

---

### 📦 Installation locale

```bash
# Cloner le repo
git clone https://github.com/ton-utilisateur/tradingv2.git
cd tradingv2

# Installer les dépendances
pip install -r requirements.txt

# Lancer l’API en local
uvicorn main:app --reload
```

---

## 🐳 Utilisation avec Docker

```bash
# Build et lancement des conteneurs
docker-compose up --build
```

Accès à l’API : [http://localhost:8000](http://localhost:8000)  
Documentation interactive : [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📌 Endpoint principal

### `GET /analyse`

Analyse les données Kline pour une paire et un intervalle donnés.

**Exemple :**

```http
GET /analyse?pair=BTCUSDT&interval=5m
```

**Réponse :**
```json
{
  "status": "success",
  "result": {
    "message": "Kline loaded for BTCUSDT on 5m"
  }
}
```

---

## 🗂 Structure du projet

```
.
├── conf/
│   └── conf.yml
├── db/
│   └── init.sql
├── src/
│   ├── Analyser.py
│   ├── Bitmart/Kline.py
│   ├── Coordinator/DataSourceCoordinator.py
│   ├── Loader/
│   │   ├── Json/BitMart/...
│   │   ├── Json/Local/...
│   │   ├── DataLoader.py
│   │   └── EnumTypeData.py
│   └── Repository/FileSystem/KlineRepository.py
├── main.py
├── entrypoint.sh
├── docker-compose.yml
├── Dockerfile.python
├── Dockerfile.sqlite
├── requirements.txt
└── identifier.sqlite
```

---

## 📃 Licence

Ce projet est open source et libre d'utilisation.

---

## 🙋 Auteur

Développé par [TonNom].
