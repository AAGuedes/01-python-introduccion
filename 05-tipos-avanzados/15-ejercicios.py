"""
Ejercicio
"""

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restante
def noSpaceList(text: str):
    """
    Receives a string and removes empty characters\n
    Returns a list
    """
    newText: str = ""

    for char in text:
        if char != " ":
            newText += char

    return list(newText)


# 2. Contar en un diccionario cuanto se repiten
# los caracteres de un string
def numCoincidences(lis: list):
    """
    Receives a list and counts the number of repeated characters\n
    Returns a dicctionary with the number of coincidences
    """
    newDictionary: dict = {}

    for char in lis:
        newDictionary[char] = lis.count(char)

    return newDictionary


# 3. Ordenar las llaves de un diccionario
# por el valor que tiene y devolver una lista
# que un listado de tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]
def dictionaryToList(dic: dict):
    """
    Receives a dictionary convert it to a list of tuples\n
    Returns a list of tuples
    """
    newList: list = []

    for key, value in dic.items():
        newList.append([key, value])

    newList.sort()

    newTupleList: list = []

    for key, value in newList:
        newTupleList.append((key, value))

    return newTupleList


# 4. De una lista de tuplas, devolver las tuplas
# que tengan el valor mayor
# [("a", 3), ("b", 2), ("c", 4) -> ("c", 4)]
def findHighestValues(tup: tuple):
    """
    Receives a tuple and return the highest value/values\n
    Returns a tuple list
    """
    newHighestValue = [("", 0)]

    for key, value in tup:

        newKey, newValue = newHighestValue[0]

        if newValue < value:
            newHighestValue.clear()
            newHighestValue.append((key, value))
        elif newValue == value:
            newHighestValue.append((key, value))

    return newHighestValue


# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con 4 repeticiones son:
# - C
# Deben estar con mayúscula
def printMessage(tuple: tuple):
    """
    Shows a message with highest values and number of coincidences\n
    """
    for key, value in tuple:
        print(f"Character {key.upper()} - {value} coincidences")


# 6. Juntar la solución de los ejercicios anteriores
# para encontrar los caracteres que más se repiten
# de un string
def main(tex: str):
    """
    Main function
    """
    list = noSpaceList(tex)
    dictionary = numCoincidences(list)
    tuple = dictionaryToList(dictionary)
    highestValues = findHighestValues(tuple)
    printMessage(highestValues)


texto: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
main(texto)
