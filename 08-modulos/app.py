"Clase app"

# from usuarios.acciones import guardar, pagar_impuestos
from usuarios.impuestos.utilidades import pagar_impuestos

pagar_impuestos()

# Otra forma de importar es la siguiente:
# import usuarios.acciones
# usuarios.acciones.guardar()

# Una alternativa más corta:
# from usuarios import acciones
# acciones.guardar()
