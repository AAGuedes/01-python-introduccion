"""
Xargs
"""


def sumar(*numeros):
    """
    Suma todos los numeros del iterable\n
    numeros (iterable)
    """
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


sumar(2, 5)
sumar(2, 5, 9)
sumar(2, 5, 9, 45, 97)
