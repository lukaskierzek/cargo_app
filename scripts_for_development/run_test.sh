#!/usr/bin/env bash
docker compose up -d --build airlift &&
echo "Enter a number of verbosity: "
read number
docker compose exec -it airlift bash -c "cd cargo_app && python manage.py test --verbosity ${number}"
docker compose kill airlift