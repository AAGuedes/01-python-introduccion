"""
Anulación de método
"""


class Bird:
    "Bird class"

    def __init__(self):
        self.flying = "Flying"

    def fly(self):
        "Fly bird"
        print("Fly bird!")


class Duck(Bird):
    "Duck class"

    def __init__(self):
        super().__init__()  # Instancia el constructor de la clase padre y trae sus propiedades
        self.swimming = "Swimming"

    def fly(self):
        "Fly duck"
        super().fly()       # Permite acceder al método de la clase padre
        print("Fly duck!")


duck = Duck()
duck.fly()

print(duck.flying, duck.swimming)
