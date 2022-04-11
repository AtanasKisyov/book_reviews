gunicorn --pythonpath book_reviews book_reviews.wsgi
release: python manage.py migrate
web: python book_review manage.py runserver