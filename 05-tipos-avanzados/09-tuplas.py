"""
Tuplas
"""

# Las tuplas son lo mismo que las listas pero no son modificables
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Se puede crear una tupla de cualquier elemento iterable
punto = tuple([1, 2])
print(punto)

# Se puede crear una nueva tupla especificando posiciones
menosNumeros = numeros[:2]
print(menosNumeros)

# Se pueden desempaquetar al igual que las listas
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Se puede crear una lista en el caso de que se necesite y esta si se podra modificar
listaNumeros = list(numeros)
print(listaNumeros)
