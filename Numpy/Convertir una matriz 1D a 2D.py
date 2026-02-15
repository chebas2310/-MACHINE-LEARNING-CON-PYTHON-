#CONVERTIR UNA MATRIZ 1D A UNA MATRIZ 2D
"""
- (np.newaxis) Agrega una nueva dimensión a una matriz
- (np.expand_dims) Agrega una nueva dimensión a una matriz en una posición específica
"""
import numpy as np

att = np.array([1,2,3,4,5,6)]

#Cada vez que uses (np.newaxis) la dimension de la matriz aumentara 1 vez
"""
Para este ejemplo usaremos el atributo (.shape) que nos da las filas x columnas
de la matriz
"""
print(att.shape)
"""
El resultado nos arrojara (6,) indicando que la matriz es de 1 dimensión, ahora usaremos (np.newaxis)
para agregar un nuevo eje
"""
att2 = att[np.newaxis, :]
print(att2.shape)
"""
Lo que le digo a python es [np.newaxis, :]
- (:) = "Quiero que coloques todos los elementos"
- (np.newaxis) = "Y colocalos en este nuevo eje"
De esta misma forma puedes crear un "vector fila" a partir de una matriz 1D
"""


#MÁS EJEMPLOS
"""
Vamos a agregar una dimensión extra a una matriz 2D
"""
A = np.array([[1,2,3,4],[5,6,7,8]])

A2 = A[: ,: , np.newaxis] #Aqui agregamos una dimension al final
print(A2.shape)
#Visualizacion: (2,3,1)

A3 = A[np.newaxis, :, :] #Aqui agregamos una dimension al comienzo
print(A3.shape)
#Visualizacion: (1,2,3)


