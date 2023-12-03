"""
Alcance
"""

# Las variables globales son una mala practica, evitar usarlas
saludo: str = "Hola global"


def saludar():
    """
    Funcion saludar
    """
#    global saludo  # Permite acceder a una variable global, evitar usar
    saludo = "Hola Mundo"


print(saludo)
saludar()
print(saludo)
