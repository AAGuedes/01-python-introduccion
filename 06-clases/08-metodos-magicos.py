"""
Metodos magicos
Más info: https://rszalski.github.io/magicmethods/
"""


class Animal:
    """
    Docstring
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal Class: {self.name}"

    def talk(self):
        """
        Doctring
        """
        print(f"{self.name}: Woof!")


animal = Animal("Perro", 7)

# Todos los métodos mágicos comienzan con __ y terminan con __
print(animal)
print(animal.__dict__)

texto = str(animal)
print(texto)
