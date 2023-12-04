"""
Filas (FIFO)
"""
from collections import deque

fila = deque([1, 2, 3, 4])
fila.append(5)
print(fila)

# Elimina el primer elemento por la izquierda
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
print(fila)

if not fila:
    print("Fila vacía")