from pathlib import Path
from zipfile import ZipFile

# Comprimir curso
with ZipFile("10-archivos\\comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        # print(path)
        if str(path) != "10-archivos\\comprimidos.zip":
            zip.write(path)


# descomprimir curso
with ZipFile("10-archivos\\comprimidos.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("10-archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    zip.extractall("10-archivos\\descomprimidos")
