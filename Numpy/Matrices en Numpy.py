#INTRODUCCION A NUMPY

"""
Matrices en Numpy:
- Todos los elementos deben ser del mismo tipo
- Una vez creada el tamaño de la matriz no se puede cambiar
- Debe ser de forma rectangular, no irregular
"""

#Para crear un matriz primero importamos el módulo de numpy
import numpy as np

#Para crear una matriz lo hacemos con (np.array)
arr = np.array([1,2,3,4,5,6])
print(arr)

print("----------------------")

#También podemos crear matrices con varias dimensiones de la sigueinte forma:
brr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(brr)
