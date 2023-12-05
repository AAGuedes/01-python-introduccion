"""
Ejemplo real de herencia
"""


class Model():
    "Model class"

    table = False

    def __init__(self):
        if not self.table:
            print("Error, must define a table")

    def save(self):
        "Save method"
        print(f"Saving {self.table} into Database")

    @classmethod
    def find(self, _id):
        "Find mehod"
        print(f"Searching user with {_id} in {self.table}")


class User(Model):
    "User class"

    table = "User"


user = User()
user.save()
user.find(1)
