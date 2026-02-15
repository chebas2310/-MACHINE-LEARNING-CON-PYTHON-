#INDEXAR Y CORTAR UNA MATRIZ

"""
Indexar y dividir matrices en Numpy se hace de la misma forma como se trabaja con listas 
en Python, por ejemplo si quieres acceder a un deto especifico dentro de una matriz lo
haces de la siguiente manera:
"""
import numpy as np

data = np.array([1,2,3,4])
print(data[1])
#Impresion: (2)
print(data[1:])
#Impresion: (2,3)
print(data[0:2])
#Impresion: (1,2)


#APLICAR CONDICIONES PARA SELECCIONAR VALORES
"""
Si deseas obtener valores especificos de una matriz segun unas condiciones
puedes hacerlo de la siguiente forma:
"""

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[a<5]) #Imprimir los valores menores a 5
#Impresion: (1,2,3,4)
print(a[a>=5]) #Imprimir los valores mayores o iguales a 5
#Impresion: (5,6,7,8,9,10,11,12)
print(a[a%2 == 0]) #Imprimir valores divisibles entre 2
#Impresion: (2,4,6,8,10,12)

"""
En caso tengas matrices con otro tipo de valores puedes usar operadores logicos (&) y (|)
que retornan valores booleanos, ellos especificaran si una matriz cumple o no una condicion.
Por ejemplo: 
"""

print((a>5)|(a==5)) #Imprimir los valores mayores o iguales a 5
#Impresion: [[False False False False]
#            [ True  True  True  True]
#            [ True  True  True  True]]







