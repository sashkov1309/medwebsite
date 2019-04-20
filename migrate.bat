@echo off
python manage.py makemigrations doctor
python manage.py makemigrations
python manage.py migrate
pause

ftype jarfileterm=cmd /s /k “”C:\Program Files (x86)\Common Files\Oracle\Java\javapath” -jar “%1″ %*”