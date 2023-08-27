#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=${DB_PASSWORD} psql -h "$host" -U "postgres" -c '\q'; do
  echo >&2 "Postgres is unavailable - sleeping"
  sleep 1
done

echo >&2 "Postgres is up - executing command"

export IS_DOCKER_COMPOSE=1
cd IIS
python manage.py migrate
python manage.py loaddata fixtures/users.json
printf "\n\n\t\tsuperuser created:\n\t\t\tlogin - admin\n\t\t\tpassword - 8Xgex7E6CRCF4wz\n\n\n"
python manage.py loaddata fixtures/groups.json
printf "\n\n\t\tgroups added:\n\t\t\tcrud\n\t\t\treadonly\n\t\t\tnone\n\n\n"
python manage.py runserver 0.0.0.0:8000

exec $cmd
