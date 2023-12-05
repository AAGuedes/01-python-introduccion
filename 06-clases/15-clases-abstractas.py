"""
Clases abstractas
"""
# Necesario importar para generar una clase abstracta
from abc import ABC, abstractmethod


class Model(ABC):
    "Model class"

    # Como la propiedad se define en la subclase, ya no es necesario el constructor
    # def __init__(self):
    #     if not self.table:
    #         print("Error, must define a table")

    # La propiedad pasa a ser decorada con las anotaciones
    @property
    @abstractmethod
    def table(self):
        "Table property"

    @abstractmethod
    def save(self):
        "Save method"

    @classmethod
    def find(self, _id):
        "Find mehod"
        print(f"Searching user with {_id} in {self.table}")


class User(Model):
    "User class"

    table = "User"

    # Es necesario implementar el método abstracto
    def save(self):
        print(f"Saving {self.table} into Database")


# model = Model() # Ya no permite instanciar la clase abstracta
user = User()
user.save()
user.find(1)
