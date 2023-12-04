"""
Propiedades de clase
"""


class Animal:
    """
    Docstring
    """

    legs = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def can_talk(self):
        """
        Doctring
        """
        print(f"{self.nombre} dice: Guau!")


mi_animal = Animal("Toby", 2)

print(Animal.legs)

print(mi_animal.legs)

mi_animal.legs = 2
print(mi_animal.legs)
