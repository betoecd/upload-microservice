#!/bin/bash
# Set ENV_PATH
export ENV_PATH=/dev.env
export DEBUG=True

#TODO: # Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

# Start server
echo "Starting server"
python manage.py grpcrunserver --dev &
gunicorn --chdir /src --bind :8000 --access-logfile - --reload AuthJwt.wsgi:application
# python manager.py runserver 0.0.0.0:8000
