"""
Operador de desempaquetamiento
"""

lista = [1, 2, 3, 4]
print(lista)

# Con el * se desempaqueta tanto listas como tuplas
print(*lista)

lista2 = [5, 6]

# Se pueden combinar listas
combinada = [*lista, *lista2]
print(combinada)

punto1 = {"a": 100, "b": 100}
punto2 = {"x": 200, "y": 200}

# También se pueden combinar diccionarios, prevalece la clave repetida en la derecha
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
