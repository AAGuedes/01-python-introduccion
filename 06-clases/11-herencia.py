"""
Herencias
"""


class Animal:
    "Animal class"

    def walk(self):
        "Walk"
        print("Walking in the moon!")

    def eat(self):
        "Eat"
        print("Eating! Nom! Nom! Nom!")


class Dog(Animal):
    "Dog class"

    def bark(self):
        "Bark"
        print("Woof!")


class Developer(Animal):
    "Developer class"

    def write(self):
        "Write"
        print("Writing code! Yay!")

# Comparte la herencia de Animal y además tiene su método propio walk
dog = Dog()
dog.walk()
dog.bark()

# Comparte la herencia de Animal y además tiene su método propio write
developer = Developer()
developer.walk()
developer.write()
