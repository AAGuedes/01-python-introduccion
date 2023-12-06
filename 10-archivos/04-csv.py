import csv
import os

ENC = "UTF-8"

# Escribir
# Si no se especifica el newline, inserta una linea vacía tras cada inserción
with open("10-archivos/archivo.csv", "w", newline="", encoding=ENC) as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["row_id", "user_id", "text"])
    writer.writerow([1, 1000000, "Some text here"])
    writer.writerow([2, 1000001, "More text here"])

# Leer
with open("10-archivos/archivo.csv", "r", encoding=ENC) as archivo:
    reader = csv.reader(archivo)
    for linea in reader:
        print(linea)

# Actualizar
with open("10-archivos/archivo.csv", encoding=ENC) as fr, open("10-archivos/temp_archivo.csv", "w", newline="", encoding=ENC) as fw:
    reader = csv.reader(fr)
    writer = csv.writer(fw)
    for linea in reader:
        print(linea)
        if linea[1] == "1000000":
            writer.writerow([linea[0], linea[1], "Edited text"])
        else:
            writer.writerow(linea)

    fr.close()
    fw.close()

    os.remove("10-archivos/archivo.csv")
    os.rename("10-archivos/temp_archivo.csv", "10-archivos/archivo.csv")
