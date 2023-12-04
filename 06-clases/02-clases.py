"""
Creando clases
"""
class Animal:
    """
    Docstring
    """

    def can_talk(self):
        """
        Doctring
        """
        print("Guau!")

my_animal = Animal()
print(type(my_animal))

my_animal.can_talk()
print(isinstance(my_animal, Animal))
