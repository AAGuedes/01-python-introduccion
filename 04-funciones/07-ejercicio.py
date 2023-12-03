"""
Ejercicio sección 4
Un palindromo es una palabra que se lee igual de izquierda a derecha como de derecha a izquierda
"""


def es_palindromo(texto):
    """
    Docstring
    """
    palindromo: str = ""
    omordnilap: str = ""
    nchar: int = 0
    resultado: bool = True

    # Primero eliminamos todos los espacios en blanco
    for char in texto:
        if char != " ":
            nchar += 1
            palindromo += char.lower()

    # Comparamos que el palindromo sea igual en ambos sentidos de lectura
    while nchar != 0:
        omordnilap += palindromo[nchar - 1]
        nchar -= 1

    # Comparamos que tanto el palidromo como el omoomordnilap son iguales
    if palindromo != omordnilap:
        resultado = False

    return resultado


print("Abba", es_palindromo("Abba"))                    # True
print("Reconocer", es_palindromo("Reconocer"))          # True
print("Amo la paloma", es_palindromo("Amo la paloma"))  # True
print("Hola Mundo", es_palindromo("Hola Mundo"))        # False
