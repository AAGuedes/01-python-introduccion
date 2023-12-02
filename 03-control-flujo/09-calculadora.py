"""
Ejercicio de calculadora
"""

print("Calculadora")
print("Para salir escriba: salir")
print("Las operaciones son: +, -, * y /")
numero1 = int(input("Ingrese el primer numero: "))
while True:
    operacion = input("Ingrese la operación: ")

    if operacion == "salir":
        break

    numero2 = int(input("Ingrese el siguiente número: "))
    if operacion == "+":
        numero1 = numero1 + numero2
    if operacion == "-":
        numero1 = numero1 - numero2
    if operacion == "*":
        numero1 = numero1 * numero2
    if operacion == "/":
        numero1 = numero1 / numero2
    print(numero1)
