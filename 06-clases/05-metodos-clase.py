"""
Metodos de clase
"""


class Animal:
    """
    Docstring
    """

    legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def can_talk(cls):
        """
        Doctring
        """
        print("Woof!")

    @classmethod
    def factory(cls):
        """
        Docstring
        """
        return cls("Happy Toby", 4)


Animal.can_talk()

animal1 = Animal("Toby", 4)
animal2 = Animal("Fleas", 2)
animal3 = Animal.factory()

print(animal3.name, animal3.age)
