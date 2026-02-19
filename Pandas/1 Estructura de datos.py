#INTRODUCCIÓN A PANDAS
"""
Pandas es una librería de código abierto para Python que se usa para la manipulación y el analisis
de datos, principalmente trabaja con datos tabulares, es decir, tablas de datos, imagina como si 
Excel y Python tuvieran un hijo.
En pandas hay 2 estructuras de datos que se manejan siempre:
- Series: Son simplemente una columna unidimencional de datos, donde cada elemento de la columna tiene
un índice.
- DataFrames: Son tablas completas con filas y columnas, ambos tienen sus respectivos índice y etiqueta
"""

import pandas as pd
import numpy as np

#Como primer ejemplo, creemos una serie a partir de un array de numpy 
list = np.array([7,4,9,2,8,10])
s = pd.Series(list)
print(s)
#Impresión:
#    0     7
#    1     4
#    2     9
#    3     2
#    4     8
#    5    10
#    dtype: int64
#En ese ejemplo, la primero columna son los índices de cada elemento de la columna
#La segunda columna son los datos de mi array
#NOTA: al final pandas siempre imprimira el tipo de dato que contiene, en este caso "int64"


#Para el siguiente ejemplo, crearemos un DataFrame, esta vez a partir de una lista de python
df = ['Toyota', 'Subaru', 'Suzuki', 'Ford', 'Tesla']
p = pd.DataFrame(df, columns = ['Cars']) #Cuando creas un DataFrame puedes añadirle un parametro extra al pd.DataFrame
print(p)                                 #esta parametro es el nombre de la etiqueta de tu columna
#Impresión:
#         Cars
#    0  Toyota
#    1  Subaru
#    2  Suzuki
#    3    Ford
#    4   Tesla


#Ahora creemos un dataframe a traves de un diccionário en python
#Este diccionario guardara una lista de pasajeros del Titanic con sus nombre, edades y sexos
nd = {
  "Name": [
    "Brandon, Mr. Owen Harris",
    "Allen, Mr. William Henry",
    "Bonnell, Miss Elizabeth",
  ]
  "Age": [22,35,58],
  "Sex": ["male", "male", "female"],
}
new_df = pd.DataFrame(nd)
print(new_df)
#Impresión: 
#                           Name  Age     Sex
#    0  Brandon, Mr. Owen Harris   22    male
#    1   Allen, Mr. William Henry   35    male
#    2   Bonnell, Miss Elizabeth   58  female






