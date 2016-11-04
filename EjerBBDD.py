import sqlite3

listaInfoLibros =  [('El Quijote', 'Miguel de Cervantes','Alianza','LIBRO','1988-06-11','España',12),('Marina', 'Carlos Ruiz Zafón','Edebé','CD','2003-05-10','España',18.95), ('La hoguera de las vanidades','Tom Wolfe','RBA editores','DVD','2005-11-09','USA',22.25), ('Los pilares de la Tierra','Ken Follet','Faber','LIBRO','2014-12-01','USA',12.95), ('Otelo','William Shakespeare','Anaya','LIBRO','2013-04-11','Inglaterra',14.95), ('Rimas y Leyendas','Gustavo Adolfo Becquer','Roca','LIBRO','2008-01-08','España',25.95), ('Poesía','Juan Ramón Jimenez','P&J','LIBRO','2002-04-07','España',10.95)]
listaInfoCompradores = [('Juan Miedo','1955-10-23','608900890','La isla del tesoro,33','Getafe','Buen comprador'), ('Pepe Pepino','1961-12-13','607899005','Plaza Mayor,56','Pozuelo',''), ('Pepe Mur','1976-04-02','917895679','Esparteros,5','Getafe',''), ('Mohamed Alí','1968-11-12','609440567','Juan sin miedo,40','Pozuelo','Le gusta la ciencia ficción'), ('Alfredo Mesa','1986-08-17','690890456','Gran vía,56','Getafe','Le gustan los ensayos'), ('Pedro Reyes','1957-08-25','917890056','Plaza de España,34','Pozuelo','Le gusta la historia'), ('Isabel Olvido','1977-07-20','915678900','Principal,3','Getafe','Le gusta la novela de terror'), ('Mariano Calcetines','1996-11-09','634567876','Aviación,34','Getafe',''), ('María Calero','1984-11-08','645666900','Río Ebro,4','Las Rozas','') ]
listaInfoCompras = [(9,7), (9,3), (8,2), (7,1), (8,1), (1,1), (7,1), (6,2), (3,5), (3,1), (3,2)]
 
def Creacion(cur):
    #Borramos si existe previamente la tabla
    cur.execute("DROP TABLE IF EXISTS Libros")
    cur.execute("DROP TABLE IF EXISTS Compras")
    cur.execute("DROP TABLE IF EXISTS Compradores")
    
    #creamos las tres tablas
    cur.execute("CREATE TABLE Libros(registro INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(35) NOT NULL,escritor VARCHAR(35) NOT NULL,editorial VARCHAR(20) NOT NULL,soporte VARCHAR(35) NOT NULL,fecha_entrada DATE NOT NULL, pais VARCHAR(20) NOT NULL, importe DECIMAL(8,2) NOT NULL, anotaciones BLOB)")
    cur.execute("CREATE TABLE Compradores(registro INTEGER PRIMARY KEY AUTOINCREMENT , nombre VARCHAR(35) NOT NULL, fecha_nacimiento DATE NOT NULL, telefono VARCHAR(10), domicilio  VARCHAR(35), poblacion  VARCHAR(25), anotaciones  TEXT)")
    cur.execute("CREATE TABLE Compras(registro INTEGER PRIMARY KEY AUTOINCREMENT, id_comprador INTEGER(4) NOT NULL, id_libro INTEGER(4) NOT NULL)")
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



