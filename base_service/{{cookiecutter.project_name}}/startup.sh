#!/bin/bash
APP_DIR=/{{cookiecutter.project_name}}
cd $APP_DIR
alembic upgrade head
cd $APP_DIR
uvicorn app.main:app --host 0.0.0.0 --port 80