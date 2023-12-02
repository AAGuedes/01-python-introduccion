"""
Calculadora
"""

numero1 = input("Ingresa el primer número: \n")
numero2 = input("Ingresa el segundo número: \n")

numero1 = int(numero1)
numero2 = int(numero2)

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

mensaje = f"""
Para los números {numero1} y {numero2} los resultados de las operaciones son:
Suma: {suma}
Resta: {resta}
Multiplicación: {multiplicacion}
Division: {division}
"""

print(mensaje)
