"""
Polimorfismo
"""

from abc import ABC, abstractmethod


class Model(ABC):
    "Model class"

    @abstractmethod
    def save(self):
        "Save abstract method"


class User(Model):
    "User class"

    def save(self):
        print("Saving in database")


class Session(Model):
    "Session class"

    def save(self):
        print("Saving file")


def save(entities):
    "Save function"
    for entity in entities:
        entity.save()


user = User()
session = Session()

# Polimorfismo: Ambos objetos cumplen con una interfaz
# necesaria para ser ejecucados por la función de guardar
save([user, session])
