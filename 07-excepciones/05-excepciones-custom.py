"""
Excepciones personalizadas
"""


class MyError(Exception):
    "Represent my custom error"

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"Error: {self.code} - {self.message}"


def divide(n=0):
    "Divide function"
    if n == 0:
        raise MyError("Can't divide by 0", "805")
    return 5 / n


try:
    divide()
except MyError as e:
    print(e)
