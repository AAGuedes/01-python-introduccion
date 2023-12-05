"""
Duck Typing
"""


class User():
    "User class"

    def save(self):
        "Save method"
        print("Saving in database")


class Session():
    "Session class"

    def save(self):
        "Save method"
        print("Saving file")

# Duck typing, python no comprueba que extienda de la clase Model
def save(entities):
    "Save function"
    for entity in entities:
        entity.save()


user = User()
session = Session()

# Polimorfismo: Ambos objetos cumplen con una interfaz
# necesaria para ser ejecucados por la función de guardar
save([user, session])
