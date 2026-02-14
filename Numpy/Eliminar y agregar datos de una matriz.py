#AGREGAR, ELIMINAR Y ORDENAR ELEMENTOS
"""
- (np.sort) Ordena los elementos de una matriz
- (np.concatenate) Concatena dos o más matrices
- (np.append) Agrega elementos al final de una matriz
"""

arr = np.array([4,6,1,8,2,3])
print(np.sort(arr))
"""
Ordenes extras para sort:
- argsort()
- lexsort()
- searchsorted()
- partition()
"""


x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])
print(np.concatenate((x,y), axis = 0))
