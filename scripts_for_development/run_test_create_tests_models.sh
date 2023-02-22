#!/usr/bin/env bash
docker compose down &&
docker compose up --build -d &&
docker compose exec -it airlift bash -c "cd cargo_app && python manage.py makemigrations" &&
docker compose exec -it airlift bash -c "cd cargo_app && python manage.py migrate" &&
docker compose exec -it airlift bash -c "cd cargo_app && python manage.py test"