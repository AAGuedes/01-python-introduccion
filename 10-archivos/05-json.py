import json
from pathlib import Path

ENC = "UTF-8"

# Escribir JSON
productos = [
    { "id": 1, "name": "Surfboard"},
    { "id": 2, "name": "Bicicleta"},
    { "id": 3, "name": "Skate"}
]
data = json.dumps(productos)
Path("10-archivos/productos.json").write_text(data, encoding=ENC)


# Leer JSON
data = Path("10-archivos/productos.json").read_text(encoding=ENC)
productos = json.loads(data)
print(productos)


# Modificar
productos[0]["name"] = "Tabla de Surf"
Path("10-archivos/productos.json").write_text(json.dumps(productos), encoding=ENC)
