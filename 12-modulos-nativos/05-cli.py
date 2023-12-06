import os
from pathlib import Path
import sys


def cli(args):
    "Función CLI"

    if len(args) == 1:
        print("No se han pasado argumentos")
        return

    if len(args) != 3:
        print("Se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[1]
    d = Path(destino)
    if not d.exists():
        print("El destino no puede existir")
        return

    os.rename(str(origen), str(destino))

    print("Archivo renombrado con éxito")


cli(sys.argv)
