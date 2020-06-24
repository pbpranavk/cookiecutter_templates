import os
import shutil

print(os.getcwd())  

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_db = '{{cookiecutter.create_db}}' == 'y'

if not create_db:
    remove('db')
