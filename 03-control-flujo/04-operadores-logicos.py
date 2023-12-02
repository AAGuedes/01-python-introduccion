"""
Operadores lógicos and, or y not
"""

GAS = False
ENCENDIDO = False
EDAD = 18

if GAS and ENCENDIDO:
    print("Puedes avanzar 1")

if GAS or ENCENDIDO:
    print("Puedes avanzar 2")

if not GAS or ENCENDIDO:
    print("Puedes avanzar 3")

if not GAS and (ENCENDIDO or EDAD > 17):
    print("Puedes avanzar 4")
