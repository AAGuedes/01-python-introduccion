"""
Tipos de excepciones
"""

try:
    number1 = int(input("Input first number: "))
except ValueError as e:
    print("Input a numeric value")
