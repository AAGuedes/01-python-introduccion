"Inyección de dependencias esta clase es teórica"

# import Correa

# Esta forma de inyectar la dependencia genera una dependencia fuerte que
# dificulta futuras implementaciones, lo ideal es pasarla como atributo
# al constructor
# class Perro:
#     def __init__(self):
#         self.correa = Correa()

# =====

# import usuario

# No facilita la reutilización
# def guardar():
#     usuario.guardar()

# Facilita la reutilización ya que la entidad implementa el guardado
# y también agiliza el testeo
# def guardar(entidad):
#     entidad.guardar()

# =====

# Algunos frameworks como Flask requieren metodos similares al siguiente:
# def init_app(bbdd, api):
    # Código...
