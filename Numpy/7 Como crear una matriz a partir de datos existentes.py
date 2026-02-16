#COMO CREAR UNA MATRIZ A PARTIR DE DATOS EXISTENTES
"""
Es este tema tocaremos las sigueintes funciones:
- (np.vstack)
- (np.hsplit)
- (.view)
- (copy)
"""

#CREAR UNA AMTRIZ A PARTIR DE UNA SECCION DE OTRA
"""
Puedes seleccionar desde donde hasta donde quieres dividir una matriz ya establecida
como el siguiente ejemplo:
"""
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
arr1 = a[1:7]
print(arr1)
#Impresion: (2,3,4,5,6,7,8)



#COMO APILAR MATRICES DE FORMA VERTICAL Y HORIZONTAL
"""
En el caso que tengas 2 matrices como a1 y a2 puedes apilarlas con las siguientes funciones:
- (vstack): para apilar verticalmente
- (hstack): para apilar horizontalmente
"""
a1 = np.array([[1,1],
               [2,2]])
a2 = np.array([[3,3],
               [4,4]])

np.vstack((a1,a2))
#Impresion: [[1, 1],
#            [2, 2],
#            [3, 3],
#            [4, 4]]

np.hstack((a1,a2))
#Impresion: [[1, 1, 3, 3],
#            [2, 2, 4, 4]]



#COMO DIVIDIR UNA MATRIZ EN VARIAS MATRICES
"""
Cuando tenemos una matriz que guarda muchos datos, podemos dividirla en varias matrices mucho más
pequeñas con la funcion: 
- (hsplit)
Se entiende mejor con el siguiente ejemplo:
"""
x = np.arange(1,25).reshape(2,12) #Crear una matriz del 1 al 25 y que se divida en 12 elementos por igual
print(x)
#Impresion: [[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
#            [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]]

"""
Si quieres dividir esta matriz en 3 matrices de formas iguales, lo hacemos de la sigueinte manera:
"""
np.hsplit(x,3)
#Impresion:  ([[ 1,  2,  3,  4],
#              [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
#              [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
#              [21, 22, 23, 24]])



#EXPLICACION SOBRE LAS COPIAS Y LAS VISTAS 
"""
Cuando creas una matriz, numpy guarda los datos en un bloque de memoria. Cuando creas una copia, numpy
copia los mismos datos en otro bloque de memoria diferente, de esa forma puedes editar un bloque y el
otro seguira sin cambios. 
Una vista es un caso contrario, aqui no creas una nueva memoria, solo una nueva forma de mirar los
mismo datos. Acontinuación algunos ejemplos:
"""
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

b1 = a[0, :] #En este guardamos todos los elementos de la 1ra fila
print(b1)
#Impresion: ([1,2,3,4]) 
b1[0] = 99 #Ahora altero el 1er elemento de la fila
print(b1)
#Impresion: [[99,  2,  3,  4],
#            [ 5,  6,  7,  8],
#            [ 9, 10, 11, 12]]
"""
Apesa de no haber alterado el valor en el mismo indice de la matriz (arr) al imprimirla el valor del
indice [0] cambio, esto ocurre porque funciones y operaciones en numpy devolveran "vistas" siempre que 
sea posible, porque ahorra memoria y es más rápido, pero modificar los datos en una vista tambien lo
hace en la matriz original.
Pero usando (copy) el método hara una copia completa de la matriz y sus datos. 
Como el sigueinte ejemplo:
"""
b2 = arr.copy()




