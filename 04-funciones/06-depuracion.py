"""
Depurando funciones
Genera un fichero llamado launch.json para depurar por que
retorna 1 en lugar de el número de carteres del String
El error era la identación del return
"""


def largo(texto):
    """
    Docstring
    """
    resultado = 0
    for _char in texto:
        resultado += 1
    return resultado


print("Breakpoint!")
l: int = largo("Hello World!")
print(l)
