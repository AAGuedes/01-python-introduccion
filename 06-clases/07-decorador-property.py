"""
Decorador properties
"""


class Animal:
    """
    Docstring
    """

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        """
        Getter for name
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Setter for name
        """
        if name.strip():
            self.__name = name
        return



animal = Animal("Perro")
print(animal.name)
