source ../venv/bin/activate
cd ../documentStore
python manage.py makemigrations apiApp
python manage.py migrate
