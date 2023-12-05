"""
Invocar excepciones
Más info: https://docs.python.org/3/library/exceptions.html
"""


def divide(n=0):
    "Divide function"
    if n == 0:
        raise ZeroDivisionError("Can't divide by 0", f"{n}")
    return 5 / n


try:
    divide()
except ZeroDivisionError as e:
    print(e)
