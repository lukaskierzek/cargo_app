#!/usr/bin/env bash
DB_NAME='cargo_app_db'
DB_USER='ca001'
docker compose exec postgres psql -U $DB_USER -d $DB_NAME