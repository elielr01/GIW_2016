import sqlite3
db = sqlite3.connect('libreria.sqlite3')
db.execute("CREATE TABLE libros (id INTEGER PRIMARY KEY, item CHAR(100) NOT NULL, cantidad INTEGER NOT NULL)")
db.execute("INSERT INTO libros (item,cantidad) VALUES ('El Quijote', 4)")
db.execute("INSERT INTO libros (item,cantidad) VALUES ('Dracula', 2)")
db.execute("INSERT INTO libros (item,cantidad) VALUES ('Guerra y Paz', 30)")
db.execute("INSERT INTO libros (item,cantidad) VALUES ('Hamlet', 1)")
db.execute("INSERT INTO libros (item,cantidad) VALUES ('Frankestein', 4)")
db.commit()
