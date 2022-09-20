import os
import re
import datetime
import time
import math

count = 0
hoy = datetime.date.today()
ruta = "C:\\Users\\Tomas\\Desktop\\Curso python\\curso python 2\\practica\\proyecto dia 9\\Mi_Gran_Directorio"
os.chdir(ruta)
patron = r'N\D{3}-\d{5}' 
print (f"FECHA DE BUSQUEDA: {hoy}")
print("ARCHIVO		 NRO. SERIE")
print ('--------------------------------')
inicio = time.time()
for (root,dirs,arch) in os.walk(ruta):
    
    for archivos in arch:
            txt = open(os.path.join(root, archivos), 'r')
            texto = txt.read()
            verificar = re.search(patron, texto) 
            
            if verificar:
                         
                         print (f"{archivos} \t {verificar.group()}")
                         count += 1
final = time.time()
print ('--------------------------------')
duracion = math.ceil(final - inicio)
print (f"Numeros encontrados: {count}")  
print (f"Duracion de la busqueda: {duracion} segundos")          
            
        

