"""
En este primer ejemplo usaremos numpy y pathlib para llenar una matriz con datos que estan
en los 3 archivos que se encuentran en esta misma carpeta. Como sabemos numpy sera la libreria
para usar las matrices donde se almacenaran los datos, pathlib es una libreria nueva que usaremos
y nos ayudara a trabajar con rutas de archivos y directorios, la necesitaremos para manejar 
los 3 archivos de datos que tenemos.

-------------------------
NOTA: (archivos.CSV)
Si has visto archivos anteriormente con esta misma extensión CSV, son archivos de texto los cuales
almacenan datos de forma estructurada, separados por coma. Son el tipo de archivo por excelencia para
trabajar con bases de datos, excel, etc.
-------------------------
"""

import numpy as np
from pathlib import Path

arr = np.zeros((3,2,3)) #Creamos una matriz de 3 dimensiones que este llena de ceros
print(id(arr)) #Pedimos que nos imprima la direccion de memoria donde se alojan los datos
print(arr) #Imprimimos la matriz con ceros

for file_count, csv_file in enumerate(Path.cwd().glob("file?.csv")):
  print(f"Analizando archivo {file_count}: {csv_file}")
  array[file_count] = np.loadtxt(csv_file.name, delimeter = ",")

print(id(arr))
print(arr)

