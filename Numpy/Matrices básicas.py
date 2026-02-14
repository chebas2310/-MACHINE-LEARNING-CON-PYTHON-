#COMO CREAR UNA MATRIZ BASICA
"""
- (np.zeros) Crea una matriz de ceros
- (np.ones) Crea una matriz de unos
- (np.empty) Crea una matriz sin inicializar (puede contener valores basura)
- (np.arange) Crea una matriz con valores consecutivos
- (np.linspace) Crea una matriz con valores igualmente espaciados entre un rango 
"""

x = np.zeros((3,4), dtype = np.int64)
print(x)

y = np.ones((3,4), dtype = np.float64)
print(y)

z = np.empty((3,4))
print(z)

"""
Al utilizar las anteriores funciones para crear matrices básicas se pueden
implementar 2 parametros:
- El primer parametro indica las dimensiones de tu matriz
- El segundo parametro indica el tipo de datos que almacenara la matriz
"""
