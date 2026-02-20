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



"""
CONOCIMIENTO PREVIO: diccionarios en Python 
Un diccionario en python es una estructura que almecena "key":"value", como su nombre lo indica
cada valor esta asignado a una clave, "key" que se utilia para llamar al valor
"""
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

#Como vimos anteriormente al usar un diccionario de python para crear una serie o dataframe las "keys" se vuelven
#las etiquetas de los índices, y los "values" los datos.




#Ahora vamos a crear una serie, a partir de un funcion numpy que me genera 5 numeros aleatorios con 
#distribución normal estandar, es decir (Media = 0, Desviacion Estandar = 1)
s = pd.Series(np.random.randn(5), index = ["a","b","c","d","e"])
print(s)
#Impresión: 
#    a    0.469112
#    b   -0.282863
#    c   -1.509059
#    d   -1.135632
#    e    1.212112
#    dtype: float64
#NOTA: mediante el parametro "index" puedes darle una etiqueta personalizada a los indices de tus filas



#Hasta ahora hemos trabajo con arreglos de datos "ndarray", pero, ¿qué ocurre cuando un dato escalar y no una arrelgo?
s2 = pd.Series(5.0, index = ["a", "b", "c", "d", "e"])
print(s2)
#Impresión: 
#    a    5.0
#    b    5.0
#    c    5.0
#    d    5.0
#    e    5.0
#    dtype: float64






