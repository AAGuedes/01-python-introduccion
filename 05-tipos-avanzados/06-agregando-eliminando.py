"""
agregar y eliminar
"""

mascotas = ["Pelusa", "Pulga", "Toby", "Kity", "Toby", "Kity"]

mascotas.insert(1, "Melvin") # Inserta en la posición indicada
print(mascotas)

mascotas.append("Pupy") # Inserta al final del listado
print(mascotas)

mascotas.remove("Toby") # Elimina la primera coincidencia
print(mascotas)

mascotas.pop(1) # Elimina el último o el elemento en el índice indicado
print(mascotas)

del mascotas[0] # Elimina el elemento en el índice indicado
print(mascotas)

mascotas.clear() # Elimina todos los elementos de una lista
print(mascotas)
