#!/usr/bin/env bash
echo "Enter a id of container: "
read number
docker cp ${number}:/cargo_app/cargo_app/airlift/migrations/0001_initial.py ./cargo_app/airlift/migrations/