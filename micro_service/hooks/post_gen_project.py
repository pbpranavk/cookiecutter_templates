import os
import shutil

print(os.getcwd())


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


create_db = "{{cookiecutter.create_db}}" == "y"
create_ai = "{{cookiecutter.create_ai}}" == "y"
create_proto = "{{cookiecutter.create_proto}}" == "y"

if not create_db:
    remove("db")
    remove("alembic.ini")
    remove("alembic")

if not create_ai:
    remove("ai")

if not create_proto:
    remove("proto")
