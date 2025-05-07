#!/bin/sh

# To update run
pip install --upgrade pip

# Install required packages (change this if needed)
pip install -r requirements/production.txt

python manage.py migrate
python manage.py test
gunicorn core.wsgi:application --bind 0.0.0.0:8000
