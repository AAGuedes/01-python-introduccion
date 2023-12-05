"""
Metodos magicos
Más info: https://rszalski.github.io/magicmethods/
Destructor
"""


class Animal:
    """
    Docstring
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Bye animal... {self.name}")

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

del animal
# print(animal) # No lo imprime, ha sido destruido
