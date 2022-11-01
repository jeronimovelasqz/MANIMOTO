import sqlite3


def connect():
    conn = sqlite3.connect("estudiantes.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY, nombre text, nombrePadre text, nombreMadre text, \
                     direccion text, telefono integer,email text, fechaNacimiento integer, genero text)")

    conn.commit()
    conn.close()


def insert(nombre=" ", nombrePadre=" ", nombreMadre=" ", direccion=" ", telefono=" ", email=" ", fechaNacimiento=" ",
           genero=" "):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",
                (nombre, nombrePadre, nombreMadre, direccion, telefono, email, fechaNacimiento, genero))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    return rows

    conn.close()


def delete(id):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM student WHERE id = ?", (id,))

    conn.commit()
    conn.close()


def update(id, nombre=" ", nombrePadre=" ", nombreMadre=" ", direccion=" ", telefono=" ", email=" ",
           fechaNacimiento=" ", genero=" "):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE student SET nombre = ? OR nombrePadre = ? OR nombreMadre = ? OR direccion = ? OR telefono = ? OR email = ? OR fechaNacimiento = ? OR genero = ?", \
        (nombre, nombrePadre, nombreMadre, direccion, telefono, email, fechaNacimiento, genero))

    conn.commit()
    conn.close()


def search(nombre=" ", nombrePadre=" ", nombreMadre=" ", direccion=" ", telefono=" ", email=" ", fechaNacimiento=" ",
           genero=" "):
    try:
        conn = sqlite3.connect("student.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM student WHERE nombre = ? OR nombrePadre = ? OR nombreMadre = ? OR direccion = ? OR telefono = ? OR email = ? OR fechaNacimiento = ? OR genero = ?",
            (nombre, nombrePadre, nombreMadre, direccion, telefono, email, fechaNacimiento, genero))
        rows = cur.fetchall()
        return rows

        conn.close()

    except:
        sqlite3.OperationalError


connect()

