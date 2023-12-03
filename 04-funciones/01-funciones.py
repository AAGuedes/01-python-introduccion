"""
Introducción a las funciones
Parámetros y argumentos
Argumentos opcionales
"""


def prueba(name, surname = ""):
    """Función de prueba que recibe un nombre, apellido y lo imprime"""
    print("Hello World!")
    print(f"Welcome {name} {surname}")


prueba("John", "Doe")
prueba("Jane")
