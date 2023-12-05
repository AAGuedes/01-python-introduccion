"Clase app"

# from usuarios.acciones import guardar, pagar_impuestos
from usuarios.impuestos.utilidades import pagar_impuestos
# import usuarios

pagar_impuestos()
print("app.py", __name__)

# print(dir(usuarios))
# print(usuarios.__name__)
# print(usuarios.__package__)
# print(usuarios.__path__)
# print(usuarios.__file__)

# Otra forma de importar es la siguiente:
# import usuarios.acciones
# usuarios.acciones.guardar()

# Una alternativa más corta:
# from usuarios import acciones
# acciones.guardar()
