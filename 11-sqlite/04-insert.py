import sqlite3


with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()
    # Para insertar datos el segundo valor ha de ser una tupla
    cursor.execute(
        "INSERT INTO usuarios VALUES(?, ?)",
        (1, "Hello World!"),
    )
