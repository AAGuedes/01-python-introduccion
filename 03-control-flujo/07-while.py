"""
Operador While
"""

# NUMERO = 1
# while NUMERO < 10:
#     print(NUMERO)
#     NUMERO += 1

# comando = ""
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
