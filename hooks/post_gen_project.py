#Vamos crear un repositorio de git inmediatamente despues de que 
#terminemos de crear nuestro proyecto con cookiecutter
import subprocess #libreria que sirve para escribir en terminal

print("Almost done!")
print("Initializing a repository...")

subprocess.call(['git','init'])
subprocess.call(['git','add','.'])
subprocess.call(['git','commit','-m','"Initial commit"'])
