#!/bin/sh

# Esperar a que la base de datos esté lista
sleep 5

# Ejecutar migraciones
python manage.py migrate

# Ejecutar el servidor
exec "$@"
