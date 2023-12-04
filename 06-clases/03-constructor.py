"""
Constructor
"""


class Animal:
    """
    Docstring
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def can_talk(self):
        """
        Doctring
        """
        print(f"{self.nombre} dice: Guau!")


mi_animal = Animal("Toby", 2)
mi_animal.can_talk()
