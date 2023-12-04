"""
Pilas (LIFO)
"""

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# Se extrae siempre el último elemento para que funcione como pila
ultimoElemento = pila.pop()
print(ultimoElemento)

# Se puede acceder al último elemento con -1
print(pila[-1])
pila.pop()
pila.pop()

# Se debe controlar que la pila no esté vacía
if not pila:
    print("Pila vacía")
