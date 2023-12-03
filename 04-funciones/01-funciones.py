"""
Introducción a las funciones
Parámetros y argumentos
Argumentos opcionales
Argumentos nombrados
"""


def prueba(name, surname=""):
    """
    Función de prueba que recibe un nombre, apellido y lo imprime\n
    name (String)\n
    surname (String)
    """
    print("Hello World!")
    print(f"Welcome {name} {surname}")


prueba("John", "Doe")
prueba("Jane")

prueba(surname="Doe", name="John")
