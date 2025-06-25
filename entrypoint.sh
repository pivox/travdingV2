#!/bin/sh

set -e  # Arrêter le script en cas d'erreur

DB_PATH="/data/db.sqlite"
INIT_SQL="/app/init.sql"

# Initialisation de la base SQLite si absente
if [ ! -f "$DB_PATH" ]; then
  echo "📦 Initialisation de la base SQLite..."
  if [ -f "$INIT_SQL" ]; then
    sqlite3 "$DB_PATH" < "$INIT_SQL"
    echo "✅ Base initialisée dans $DB_PATH"
  else
    echo "⚠️ Fichier init.sql introuvable, base non initialisée."
  fi
else
  echo "✔️ Base déjà présente à $DB_PATH"
fi

# Démarrage du serveur FastAPI avec reload
echo "🚀 Lancement de FastAPI (avec reload)..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
