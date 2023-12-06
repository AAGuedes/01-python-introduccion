"Directorios"

from pathlib import Path

path = Path("09-rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("nuevo-directorio")

# Obtiene todos los nombres de los ficheros del directorio especificado
archivos = [p for p in path.iterdir() if not p.is_dir()]

# Obtiene solo aquellos que cumplen la expresión
archivos = [p for p in path.glob("02-*.py")]

# Todos los archivos de manera recursiva
archivos = [p for p in path.glob("**/*.py")]
archivos = [p for p in path.rglob("*.py")]

print(archivos)
