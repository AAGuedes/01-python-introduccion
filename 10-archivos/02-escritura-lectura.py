from pathlib import Path

archivo = Path("10-archivos/archivo_prueba.txt")

# Retorna una lista separada por cada salto de línea
texto = archivo.read_text(encoding="UTF-8").split("\n")

print(texto)

texto.insert(0, "Hello World!")

# Interpreta cada elemento de la lista como una línea
archivo.write_text("\n".join(texto), "UTF-8")
