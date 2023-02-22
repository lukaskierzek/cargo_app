#!/usr/bin/env bash
docker compose up -d --build airlift &&
docker compose exec -it airlift bash -c "cd cargo_app && python manage.py test --verbosity 1"
docker compose kill airlift