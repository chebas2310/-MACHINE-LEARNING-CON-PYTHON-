#ATRIBUTOS DE MATRICES
"""
- (.ndim) Número de dimensiones
- (.shape) Tupla con el número de filas y columnas
- (.size) Número total de elementos
- (.dtype) Tipo de datos de los elementos
"""
import numpy as np

a = np.array([1,2,3,4,5,6])

print("Numero de dimensiones es: ", a.ndim)
print("La forma de la matriz es: ", a.shape)
print("El numero total de elementos es: ", a.size)
print("El tipo de dato de los elementos es: ", a.dtype)
