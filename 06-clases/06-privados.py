"""
Propiedades y métodos privados
"""


class Animal:
    """
    Docstring
    """

    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        """
        Getter for name
        """
        return self.__name

    def set_name(self, name):
        """
        Setter for name
        """
        self.__name = name

    def can_talk(self):
        """
        Doctring
        """
        print(f"{self.__name}: Woof!")

    @classmethod
    def factory(cls):
        """
        Docstring
        """
        return cls("Happy Toby", 4)


animal = Animal.factory()
animal.can_talk()

print(animal.get_name())

# Imprime las propiedades de una clase
print(animal.__dict__)

# Permite acceder directamente a una propiedad privada (No debe usarse)
print(animal._Animal__name)
