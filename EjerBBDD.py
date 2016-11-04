import sqlite3

listaInfoLibros =  [('El Quijote', 'Miguel de Cervantes','Alianza','LIBRO','1988-06-11','España',12),('Marina', 'Carlos Ruiz Zafón','Edebé','CD','2003-05-10','España',18.95), ('La hoguera de las vanidades','Tom Wolfe','RBA editores','DVD','2005-11-09','USA',22.25), ('Los pilares de la Tierra','Ken Follet','Faber','LIBRO','2014-12-01','USA',12.95), ('Otelo','William Shakespeare','Anaya','LIBRO','2013-04-11','Inglaterra',14.95), ('Rimas y Leyendas','Gustavo Adolfo Becquer','Roca','LIBRO','2008-01-08','España',25.95), ('Poesía','Juan Ramón Jimenez','P&J','LIBRO','2002-04-07','España',10.95)]
listaInfoCompradores = [('Juan Miedo'), ('Pepe Pepino'), ('Pepe Mur'), ('Mohamed Alí'), ('Alfredo Mesa'), ('Pedro Reyes') ]
listaInfoCompras = [(9,7), (9,3), (8,2), (7,1), (8,1), (1,1), (7,1), (6,2), (3,5), (3,1), (3,2)]
 
def Creacion(cur):
    #Borramos si existe previamente la tabla
    cur.execute("DROP TABLE IF EXISTS Libros")
    cur.execute("DROP TABLE IF EXISTS Compras")
    cur.execute("DROP TABLE IF EXISTS Compradores")
    
    #creamos las tres tablas
    cur.execute("CREATE TABLE Libros(registro INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT,escritor TEXT,editorial TEXT,soporte TEXT,fecha_entrada TEXT, pais TEXT, importe FLOAT, anotaciones TEXT)")
    cur.execute("CREATE TABLE Compradores(registro INTEGER PRIMARY KEY AUTOINCREMENT , nombre TEXT NOT NULL, fecha_nacimiento TEXT, telefono INTEGER, domicilio  TEXT, poblacion  TEXT, anotaciones  TEXT)")
    cur.execute("CREATE TABLE Compras(registro INTEGER PRIMARY KEY AUTOINCREMENT, id_comprador INTEGER, id_libro INTEGER)")
    #cerramos el cursor
    cur.close()


def Programa():
    conn = sqlite3.connect('Libreria.sqlite3')
    cur = conn.cursor()
    Creacion(cur)
    conn.commit()

def CompletarTablas(cur):
    cur.executemany('INSERT INTO Libros (titulo, escritor, editorial, soporte, fecha_entrada,pais,importe) VALUES ( ?, ?) ',listaInfoLibros)
    cur.executemany('INSERT INTO Compradores (nombre, fecha_nacimiento,telefono, domicilio,poblacion,anotaciones) VALUES ( ?, ?) ',listaInfoCompradores)
    cur.executemany('INSERT INTO Compras (id_comprador, id_libro) VALUES ( ?, ?) ',listaInfoCompras)






Programa()



