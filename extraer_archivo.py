import zipfile
import os
ruta = "C:\\Users\\Tomas\\Desktop\\Curso python\\curso python 2\\practica\\proyecto dia 9"
os.chdir(ruta)
mi_zip = zipfile.ZipFile("Proyecto+Dia+9.zip", "r")
mi_zip.extractall()