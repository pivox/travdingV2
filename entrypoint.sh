#!/bin/sh

DB_PATH="/data/db.sqlite"
INIT_SQL="/app/init.sql"

# Si la base n'existe pas, on l'initialise
if [ ! -f "$DB_PATH" ]; then
  echo "Initialisation de la base SQLite..."
  sqlite3 "$DB_PATH" < "$INIT_SQL"
  echo "Base initialisée dans $DB_PATH"
else
  echo "Base déjà présente à $DB_PATH"
fi

# Démarre l’application principale
exec python /app/main.py --mode=api
