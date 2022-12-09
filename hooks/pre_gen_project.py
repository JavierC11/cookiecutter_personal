#Con este hook podemos asegurarnos que el nombre de nuestro
#archivo nunca inicie con numero
import os
import sys

project_slug = "{{ cookiecutter.project_slug}}"

if project_slug[0].isnumeric():   
    print("Is  not a valid name for this templante")
    sys.exit(1)

print("This is a valid name for the templante")