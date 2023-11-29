#!/bin/sh

python viajesrebollo/manage.py makemigrations
python viajesrebollo/manage.py migrate
python viajesrebollo/manage.py runserver 0.0.0.0:8000
