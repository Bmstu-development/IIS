#!/bin/sh

echo "waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "postgres started!"

python manage.py flush --no-input
python manage.py migrate
python manage.py loaddata IIS/fixtures/users.json

exec "$@"