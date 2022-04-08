web: gunicorn --pythonpath book_reviews book_reviews.wsgi
release: python book_review/manage.py migrate
web: python book_review/manage.py runserver 0.0.0.0:$PORT