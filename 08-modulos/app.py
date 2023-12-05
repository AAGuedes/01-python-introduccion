"Clase app"

# from usuarios.acciones import guardar, pagar_impuestos
from usuarios.acciones.utilidades import guardar, pagar_impuestos

guardar()

pagar_impuestos()

# Otra forma de importar es la siguiente:
# import usuarios.acciones
# usuarios.acciones.guardar()

# Una alternativa más corta:
# from usuarios import acciones
# acciones.guardar()
