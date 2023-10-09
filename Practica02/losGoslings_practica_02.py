# Integrantes: Santiago Romo, Maria Jose Gamba, Mateo Serrato y Diego Gabriel Hernandez

import os
import time
import shutil

dir_principal = os.getcwd()  # obtiene la direccion del directorio principal
dir_modules = dir_principal + "/modules"  # path del directorio "modules"
dir_c1 = dir_principal + "/c1"  # path de la carpeta c1
dir_c2 = dir_principal + "/c2"  # path de la carpeta c2
dir_readme = dir_modules + "/README.txt"  # path del archivo dentro del directorio "modules"
dir_archivo_c1 = dir_c1 + "/archivo_c1.txt"  # path del archivo "c1" dentro de la carpeta "c1"
dir_archivo_c2 = dir_c2 + "/archivo_c2.txt"  # path del archivo "c2" dentro de la carpeta "c2"
dir_modules_archivo_c1 = dir_modules + "/archivo_c1.txt"  # path del archivo "c1" dentro de la carpeta "modules"
dir_modules_archivo_c2 = dir_modules + "/archivo_c2.txt"  # path del archivo "c2" dentro de la carpeta "modules"
dir_modules_archivo_c1_copia = dir_modules + "/archivo_c1_copia.txt"  # path del archivo de la copia de "c1" dentro de la carpeta "modules"
dir_modules_archivo_c2_copia = dir_modules + "/archivo_c2_copia.txt"  # path del archivo de la copia de "c2" dentro de la carpeta "modules"

print("Direccion actual:", os.getcwd())  # imprime la direccion principal
print("Archivos o carpetas en la direccion:", os.listdir())  # imprime las entradas en el directorio principal

try:
    os.mkdir("modules")  # crea el directorio "modules"
    os.chdir(dir_modules)  # cambia la direccion actual al directorio "modules"
    with open("README.txt", "w") as README:  # crea README.txt que se va a interpretar como README
        README.write("Este es un archivo README")  # escribe la cadena dentro de README
except:
    print("El directorio modules ya existe")  # avisa si ya existe el directorio

size = os.path.getsize(dir_readme)  # obtiene el tamaño del archivo README
modifico_tiempo = os.path.getmtime(dir_readme)  # obtiene cuando se modifico el archivo README en tiempo unix
creo_tiempo = os.path.getctime(dir_readme)  # obtiene cuando se creo el archivo README en tiempo unix

modifico_tiempo = time.ctime(modifico_tiempo)  # convierte tiempo unix a modifico
creo_tiempo = time.ctime(creo_tiempo)  # convierte tiempo unix a creo

print("Tamaño del archivo README:", size, "bytes")  # imprime el tamaño del archivo README
print("La ultima vez que se modifico el archivo README:",
      modifico_tiempo)  # imprime el tiempo de modificacion del archivo README
print("El  archivo README se creo:", creo_tiempo)  # imprime el tiempo de creacion del archivo README

try:
    shutil.copy(dir_archivo_c1, dir_modules)  # copia el archivo c1 al directorio modules
    os.rename(dir_modules_archivo_c1,
              dir_modules_archivo_c1_copia)  # renombra el archivo "c1" en "modules" a "archivo_c1_copia.txt"
except:
    print("El archivo", dir_archivo_c1, "no existe")  # si no existe avisa al usuario

try:
    shutil.copy(dir_archivo_c2, dir_modules)  # copia el archivo c2 al directorio modules
    os.rename(dir_modules_archivo_c2,
              dir_modules_archivo_c2_copia)  # renombra el archivo "c2" en "modules" a "archivo_c2_copia.txt"
except:
    print("El archivo", dir_archivo_c2, "no existe")  # si no existe avisa al usuario

if os.path.exists(dir_archivo_c1):
    os.chdir(dir_c1)  # cambia la direccion actual a la carpeta "c1"
    print("En la carpeta c1 se encontraron los archivos:", os.listdir(),
          "y han sido eliminados")  # imprime los archivos encontrados
    os.remove(dir_archivo_c1)  # borra el archivo en la carpeta "c1"

if os.path.exists(dir_archivo_c2):
    os.chdir(dir_c2)  # cambia la direccion actual a la carpeta "c2"
    print("En la carpeta c2 se encontraron los archivos:", os.listdir(),
          "y han sido eliminados")  # imprime los archivos encontrados
    os.remove(dir_archivo_c2)  # borra el archivo en la carpeta "c2"

print("FIN DEL PROGRAMA")
