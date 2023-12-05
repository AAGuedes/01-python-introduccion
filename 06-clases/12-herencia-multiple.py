"""
Herencia múltiple
"""


class Animal:
    "Animal class"

    def walk(self):
        "Walk"
        print("Walking in the moon!")

    def eat(self):
        "Eat"
        print("Eating! Nom! Nom! Nom!")

    def talk(self):
        "Talk"
        print("What!?")


class Dog:
    "Dog class"

    def talk(self):
        "Bark"
        print("Woof!")


class Developer(Animal, Dog):
    "Developer class"

    def write(self):
        "Write"
        print("Writing code! Yay!")


# Comparte la herencia de Animal y Dog, los métodos repetidos
# se omitirán, quedandose los declarados de izquierda a derecha
developer = Developer()
developer.talk()
developer.walk()
developer.write()
