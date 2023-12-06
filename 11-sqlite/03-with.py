import sqlite3


with sqlite3.connect("11-sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCGAR(50));
        """
    )
