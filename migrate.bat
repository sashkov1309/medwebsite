@echo off
python manage.py makemigrations doctor
python manage.py makemigrations
python manage.py migrate
pause