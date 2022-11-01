import sqlite3


def connect():
    con = sqlite3.connect('saldos.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS saldos (id INTEGER PRIMARY KEY, recibo integer, nombre text, admision text, fecha integer, \
                    facultad text, semestre text, total integer, pago integer, pagare integer)')

    con.commit()
    con.close()


def insert(recibo=' ', nombre=' ', admision=' ', fecha=' ', facultad=' ', semestre=' ', total=' ', pago=' ',
           pagare=' '):
    con = sqlite3.connect('saldos.db')
    cur = con.cursor()

    cur.execute('INSERT INTO saldos VALUES (NULL,?,?,?,?,?,?,?,?,?)',
                (recibo, nombre, admision, fecha, facultad, semestre, total, pago, pagare))

    con.commit()
    con.close()


def view():
    con = sqlite3.connect('saldos.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM saldos')
    row = cur.fetchall()
    return row

    con.commit()


def delete(id):
    con = sqlite3.connect('saldos.db')
    cur = con.cursor()

    cur.execute('DELETE FROM saldos WHERE id = ?', (id,))

    con.commit()
    con.close()


def update(id, recibo=' ', nombre=' ', admision=' ', fecha=' ', facultad=' ', semestre=' ', total=' ', pago=' ',
           pagare=' '):
    con = sqlite3.connect('saldos.db')
    cur = con.cursor()

    cur.execute('UPDATE saldos SET recibo = ? OR nombre = ? OR admision = ? OR fecha = ? OR facultad = ? OR semestre = ? OR total = ? OR \
                    pago = ? OR pagare = ?', (recibo, nombre, admision, fecha, facultad, semestre, total, pago, pagare))

    con.commit()
    con.close()


def search(recibo=' ', nombre=' ', admision=' ', fecha=' ', facultad=' ', semestre=' ', total=' ', pago=' ',
           pagare=' '):
    con = sqlite3.connect('saldos.db')
    cur = con.cursor()

    cur.execute(
        'SELECT * FROM saldos WHERE  recibo = ? OR nombre = ? OR admision = ? OR fecha = ? OR facultad = ? OR semestre = ? OR total = ? OR pago = ? OR pagare = ?',
        (recibo, nombre, admision, fecha, facultad, semestre, total, pago, pagare))
    row = cur.fetchall()
    return row

    con.commit()


connect()

