"""
Sets
"""

# Un set es un grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
# print(primer)

# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo) # Convierte la lista a un set
print(segundo)

print(primer | segundo) # Operador unión para combinar sets

print(primer & segundo) # Operador intersercción imprime las coincidencias

print(primer - segundo) # Operador diferencia imprime los valores de primer que no están en segundo

print(primer ^ segundo) # Operador diferencia simétrica imprime los que no estén duplicados
