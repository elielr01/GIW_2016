import sqlite3
from bottle import route, run, template

@route('/libreria')
def mostrar_libros():
    db = sqlite3.connect('libreria.sqlite3')
    c = db.cursor()
    c.execute("SELECT item,cantidad FROM libros")
    data = c.fetchall()
    c.close()
    output = template('mostrar_libros', rows=data)
    return output

run(host='0.0.0.0', port=8080)
