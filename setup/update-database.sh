source ../venv/bin/activate
cd ../documentStore
python manage.py makemigrations
python manage.py migrate
