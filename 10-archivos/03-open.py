from io import open
from pathlib import Path

# Escritura
texto = "Hello World!"

archivo = open("10-archivos/open_archivo.txt", "w", encoding="UTF-8")
archivo.write(texto)
archivo.close()


# Lectura
archivo = open("10-archivos/open_archivo.txt", "r", encoding="UTF-8")
texto = archivo.read()
archivo.close()
print(texto)


# Lectura como lista
archivo = open("10-archivos/open_archivo.txt", "r", encoding="UTF-8")
texto = archivo.readlines()
archivo.close()
print(texto)


# Usando with se cerrarán automáticamente los archivos
# Usa el método mágico __enter__ al abrirlo
# Usa el método mágico __exit__ al cerrarlo
with open("10-archivos/open_archivo.txt", "r", encoding="UTF-8") as archivo:
    # Trae el contenido del fichero a memoria e imprime
    print(archivo.readlines())

    # El puntero tiene que ser reiniciado
    archivo.seek(0)
    for linea in archivo:
        print(linea)


# Agregar
archivo = open("10-archivos/open_archivo.txt", "a+", encoding="UTF-8")
archivo.write("A new line!")
archivo.close()


# Lectura y escritura
with open("10-archivos/open_archivo.txt", "r+", encoding="UTF-8") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "A new first line!"
    archivo.writelines(texto)


# Eliminamos el fichero al terminar
archivo = Path("10-archivos/open_archivo.txt")
archivo.unlink()
