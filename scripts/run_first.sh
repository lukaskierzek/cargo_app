#!/usr/bin/env bash
D_C='docker compose'
E_A_PY_MANAGE='exec airlift python cargo_app/manage.py'

$D_C up -d &&
$D_C $E_A_PY_MANAGE makemigrations &&
$D_C $E_A_PY_MANAGE migrate &&
$D_C $E_A_PY_MANAGE createsuperuser