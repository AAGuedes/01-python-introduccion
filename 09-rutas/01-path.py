"Introducción a rutas"

from pathlib import Path

# Path(r"C:\Archivos de Programa\Ultimate Python") # Raw String
# Path("usr/bin") # Ruta absoluta
# Path()
# Path().home()
# Path("one/__init__.py") # Ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("fichero.exe")
print(p)

p = path.with_suffix(".bat")
print(p)

p = path.with_stem("new")
print(p)
