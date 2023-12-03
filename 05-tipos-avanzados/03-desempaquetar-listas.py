"""
Desempaquetar listas
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

primero, segundo, *otros, penultimo, ultimo = numeros
print(primero, segundo, otros, penultimo, ultimo)
