"Inyección de dependencias esta clase es teórica"
"Import dínamico de paquetes"

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

# =====
# Import dinámico de paquetes
from pathlib import Path
# import db
# import graphql
# import api

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "Base de datos",
    "api": "Conexión API",
    "graphql": "Graphql"
}

def load(p):
    "Función load"
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene función __init__")


list(map(load, paths))
