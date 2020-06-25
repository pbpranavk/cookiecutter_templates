#!/bin/bash
APP_DIR=/{{cookiecutter.project_name}}
cd $APP_DIR
alembic upgrade head
cd $APP_DIR
python rpc_server.py