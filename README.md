# Cargo app
This is a project to manage aircraft cargo.

## Backend
I use Django, PostgreSQL, Nginx and Gunicorn.

## How to run
You need to install Docker. After installing Docker, use the command ```sh scripts/run_first.sh``` to the first launch of the application.

For the next application launch, use the command ```docker compose up```.

If you want to connect to the database use the command ```sh scripts/connect_to_database.sh```.

If you want to enter to webpage type ```localhost:80```.

If you want to enter to pgadmin type ```localhost:5050```.