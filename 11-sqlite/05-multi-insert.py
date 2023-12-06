import sqlite3


with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Primero"),
        (3, "Segundo"),
    ]

    cursor.executemany(
        "INSERT INTO usuarios VALUES(?, ?)",
        usuarios
    )
