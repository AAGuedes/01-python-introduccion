"""

"""

numeros = [2, 5, 156, 3526, 75, 66]

# Modifica la lista
numeros.sort()
print(numeros)

# Modifica la lista
numeros.sort(reverse=True)
print(numeros)

# Retorna una nueva lista
numeros2 = sorted(numeros)
print(numeros2)

# Retorna una nueva lista
numeros3 = sorted(numeros, reverse=True)
print(numeros3)

usuarios = [
    ["Pepe", 4],
    ["Felipe", 1],
    ["Ana", 5]
]
# Ordena por el primer elemento
usuarios.sort()
print(usuarios)


def ordena(elemento):
    """
    Retorna la posición del elemento para ordenar con sort
    """
    return elemento[1]


# Se le pasa como parámetro la key por la que ordenará
usuarios.sort(key=ordena)
print(usuarios)

usuarios.sort(key=ordena, reverse=True)
print(usuarios)
