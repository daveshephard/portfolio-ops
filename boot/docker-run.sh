#!/bin/bash

source /opt/venv/bin/activate
cd /code

python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py auto_admin
#python manage.py sendtestemail --admins

# Bind to Railway's dynamic port
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8080}

exec gunicorn p53ai.wsgi:application --bind "$HOST:$PORT"