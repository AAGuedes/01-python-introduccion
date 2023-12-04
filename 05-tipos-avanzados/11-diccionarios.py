"""
Diccionarios
"""

# Los diccionarios está formados por clave y valor
punto = {
    "x": 150,
    "y": 150
}
print(punto)
print(punto["x"])

# Se le puede agregar nuevos valores
punto["z"] = 45
print(punto)

# Si se intenta acceder a una clave que no existe, lanzará error
# Es necesario controlar que no ocurra
if "a" in punto:
    print("Encontrado", punto["a"])

# Se recomienda usar el método get ya que controla el posible error
print(punto.get("x"))
print(punto.get("a"))

# Se le puede asignar un valor por defecto en caso de que no exista
print(punto.get("a", 100))

# Se pueden eliminar valores
del punto["x"]
punto.pop("y")
print(punto)

# Se puede iterar con un for, pero no es correcto
# for clave in punto:
#     print(clave, punto[clave])

# La forma correcta es usando items() y se puede desempaquetar
punto["x"] = 200
for clave, valor in punto.items():
    print(clave, valor)

# Un uso más realizas de un diccionario sería el siguiente:
usuarios = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Doe"},
    {"id": 3, "name": "Miguel Doe"},
    {"id": 4, "name": "Maria Doe"},
]
for usuario in usuarios:
    print(usuario.get("name"))
