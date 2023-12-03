"""
Alcance
"""

saludo = "Hola global" # Las variables globales son una mala practica, evitar usarlas

def saludar():
    global saludo # Permite acceder a una variable global, evitar usar
    saludo = "Hola Mundo"

def saludaJohn():
    saludo = "John Doe"


print(saludo)
saludar()
print(saludo)
