#!/usr/bin/env bash
docker compose down &&
docker compose up --build -d &&
docker compose exec -it airlift bash -c "cd cargo_app &&
                                         python manage.py makemigrations &&
                                         python manage.py migrate &&
                                         python manage.py test"