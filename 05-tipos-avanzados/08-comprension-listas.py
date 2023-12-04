"""
Comprension listas
"""

usuarios = [
    ["Pepe", 4],
    ["Felipe", 1],
    ["Ana", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Filtrar
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# Filtrar
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# Filtrar y transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
