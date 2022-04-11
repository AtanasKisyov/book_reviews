gunicorn --pythonpath book_reviews book_reviews.wsgi
release: python manage.py makemigrations
release: python manage.py migrate
web: python manage.py runserver