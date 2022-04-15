#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
echo "Running in $APP_ENV mode"
if [[ $APP_ENV == 'production' ]]; then
    gunicorn recipe_book.wsgi:application --bind 0.0.0.0:8000 --timeout 900
else
    python manage.py runserver 0.0.0.0:8000
fi
