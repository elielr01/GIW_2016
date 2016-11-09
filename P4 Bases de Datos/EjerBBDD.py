import sqlite3

listaInfoLibros = [(u'El Quijote', u'Miguel de Cervantes',u'Alianza',u'LIBRO',u'1988-06-11',u'España',12),
                    (u'Marina', u'Carlos Ruiz Zafón',u'Edebé',u'CD',u'2003-05-10',u'España',18.95),
                    (u'La hoguera de las vanidades',u'Tom Wolfe',u'RBA editores',u'DVD',u'2005-11-09',u'USA',22.25),
                    (u'Los pilares de la Tierra',u'Ken Follet',u'Faber',u'LIBRO',u'2014-12-01',u'USA',12.95),
                    (u'Otelo',u'William Shakespeare',u'Anaya',u'LIBRO',u'2013-04-11',u'Inglaterra',14.95),
                    (u'Rimas y Leyendas',u'Gustavo Adolfo Becquer',u'Roca',u'LIBRO',u'2008-01-08',u'España',25.95),
                    (u'Poesía',u'Juan Ramón Jimenez',u'P&J',u'LIBRO',u'2002-04-07',u'España',10.95)]

listaInfoCompradores = [(u'Juan Miedo',u'1955-10-23',u'608900890',u'La isla del tesoro,33',u'Getafe',u'Buen comprador'),
                        (u'Pepe Pepino',u'1961-12-13',u'607899005',u'Plaza Mayor,56',u'Pozuelo',u''),
                        (u'Pepe Mur',u'1976-04-02',u'917895679',u'Esparteros,5',u'Getafe',u''),
                        (u'Mohamed Alí',u'1968-11-12',u'609440567',u'Juan sin miedo,40',u'Pozuelo',u'Le gusta la ciencia ficción'),
                        (u'Alfredo Mesa',u'1986-08-17',u'690890456',u'Gran vía,56',u'Getafe',u'Le gustan los ensayos'),
                        (u'Pedro Reyes',u'1957-08-25',u'917890056',u'Plaza de España,34',u'Pozuelo',u'Le gusta la historia'),
                        (u'Isabel Olvido',u'1977-07-20',u'915678900',u'Principal,3',u'Getafe',u'Le gusta la novela de terror'),
                        (u'Mariano Calcetines',u'1996-11-09',u'634567876',u'Aviación,34',u'Getafe',u''),
                        (u'María Calero',u'1984-11-08',u'645666900',u'Río Ebro,4',u'Las Rozas',u'') ]

listaInfoCompras = [(9,7), (9,3), (8,2), (7,1), (8,1), (1,1), (7,1), (6,2), (3,5), (3,1), (3,2)]

def Programa():
    conn = sqlite3.connect('Libreria.sqlite3')
    conn.text_factory = unicode
    cur = conn.cursor()
    Creacion(cur)
    CompletarTablas(cur)
    PaisesCompras(cur)
    #cerramos el cursor
    cur.close()
    conn.commit()


###################################### Creación de la base de datos y sus tablas ######################################
def Creacion(cur):
    #Borramos si existe previamente la tabla
    cur.execute(u"DROP TABLE IF EXISTS Libros")
    cur.execute(u"DROP TABLE IF EXISTS Compras")
    cur.execute(u"DROP TABLE IF EXISTS Compradores")

    #creamos las tres tablas
    cur.execute(u"""
        CREATE TABLE Libros(registro INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(35) NOT NULL,
            escritor VARCHAR(35) NOT NULL, editorial VARCHAR(20) NOT NULL, soporte VARCHAR(35) NOT NULL,
            fecha_entrada DATE NOT NULL, pais VARCHAR(20) NOT NULL, importe DECIMAL(8,2) NOT NULL, anotaciones BLOB)""")

    cur.execute(u"""
        CREATE TABLE Compradores(registro INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(35) NOT NULL,
            fecha_nacimiento DATE NOT NULL, telefono VARCHAR(10), domicilio  VARCHAR(35), poblacion  VARCHAR(25),
            anotaciones  TEXT)""")

    cur.execute(u"""
        CREATE TABLE Compras(registro INTEGER PRIMARY KEY AUTOINCREMENT, id_comprador INTEGER(4) NOT NULL,
            id_libro INTEGER(4) NOT NULL)""")


def CompletarTablas(cur):
    cur.executemany(u'INSERT INTO Libros (titulo, escritor, editorial, soporte, fecha_entrada,pais,importe) VALUES ( ?, ?, ? ,?, ? ,?, ?) ',listaInfoLibros)
    cur.executemany(u'INSERT INTO Compradores (nombre, fecha_nacimiento,telefono, domicilio,poblacion,anotaciones) VALUES ( ?, ?, ?, ?, ? ,?) ',listaInfoCompradores)
    cur.executemany(u'INSERT INTO Compras (id_comprador, id_libro) VALUES ( ?, ?) ',listaInfoCompras)

def PaisesComprasFIRST(cur):

    #Cogemos los libros y sus ventas individuales y los guardamos en un diccionario
    cur.execute("SELECT comprador,libro FROM Compras")
    diccionario= dict()
    for (comprador,libro) in cur.fetchall():
        if(libro in diccionario):
            diccionario[libro]+=1
        else:
            diccionario[libro] = 1

    #print diccionario

    #Cogemos los paises asociados a cada libro y vamos calculando su numero de ventas total
    ventasPorPais = dict()

    for libro in diccionario:
        cur.execute("SELECT pais FROM Libros WHERE registro=?", [libro])
        pais = cur.fetchone()
        #print pais
        if pais in ventasPorPais :
            ventasPorPais[pais] += diccionario[libro]
        else:
            ventasPorPais[pais] = diccionario[libro]

    #Lo ordenamos de forma inversa
    ventasPorPais.sort()
    ventasPorPais.reverse()

    #los imprimimos
    for pais in ventaPorPais:
        print pais + ": " + ventaPorPais[pais]

def PaisesCompras(cur):

    # Esta query obtiene la cantidad de libros por país ordenados por su total de ventas
    query = cur.execute(u"""
        WITH temp AS (
            SELECT pais, COUNT(pais) AS libros_vendidos, SUM(importe) AS total_ventas
            FROM Compras c, Libros l
            WHERE c.id_libro = l.registro
            GROUP BY pais
            ORDER BY total_ventas DESC )
        SELECT pais, libros_vendidos
        FROM temp
        """)

    # Ahora se imprime con un poco de formato
    print u"Ventas por pais:\n"

    for tupla in query:
        for value in tupla:
            if type(value) == unicode:
                value.encode("utf-8")
            print value,
        print "\n"



Programa()
