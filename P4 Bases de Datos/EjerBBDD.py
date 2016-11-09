import sqlite3

listaInfoLibros = [(1,u'El Quijote', u'Miguel de Cervantes',u'Alianza',u'LIBRO',u'1988-06-11',u'España',12),
                    (2,u'Marina', u'Carlos Ruiz Zafón',u'Edebé',u'CD',u'2003-05-10',u'España',18.95),
                    (3,u'La hoguera de las vanidades',u'Tom Wolfe',u'RBA editores',u'DVD',u'2005-11-09',u'USA',22.25),
                    (4,u'Los pilares de la Tierra',u'Ken Follet',u'Faber',u'LIBRO',u'2014-12-01',u'USA',12.95),
                    (5,u'Otelo',u'William Shakespeare',u'Anaya',u'LIBRO',u'2013-04-11',u'Inglaterra',14.95),
                    (6,u'Rimas y Leyendas',u'Gustavo Adolfo Becquer',u'Roca',u'LIBRO',u'2008-01-08',u'España',25.95),
                    (7,u'Poesía',u'Juan Ramón Jimenez',u'P&J',u'LIBRO',u'2002-04-07',u'España',10.95)]

listaInfoCompradores = [(1,u'Juan Miedo',u'1955-10-23',u'608900890',u'La isla del tesoro,33',u'Getafe',u'Buen comprador'),
                        (2,u'Pepe Pepino',u'1961-12-13',u'607899005',u'Plaza Mayor,56',u'Pozuelo',u''),
                        (3,u'Pepe Mur',u'1976-04-02',u'917895679',u'Esparteros,5',u'Getafe',u''),
                        (4,u'Mohamed Alí',u'1968-11-12',u'609440567',u'Juan sin miedo,4',u'Pozuelo',u'Le gusta la ciencia ficción'),
                        (5,u'Alfredo Mesa',u'1986-08-17',u'690890456',u'Gran vía,56',u'Getafe',u'Le gustan los ensayos'),
                        (6,u'Pedro Reyes',u'1957-08-25',u'917890056',u'Plaza de España,34',u'Pozuelo',u'Le gusta la historia'),
                        (7,u'Isabel Olvido',u'1977-07-20',u'915678900',u'Principal,3',u'Getafe',u'Le gusta la novela de terror'),
                        (8,u'Mariano Calcetines',u'1996-11-09',u'634567876',u'Aviación,34',u'Getafe',u''),
                        (9,u'María Calero',u'1984-11-08',u'645666900',u'Río Ebro,4',u'Las Rozas',u'') ]

listaInfoCompras = [(1,9,7), (2,9,3), (3,8,2), (4,7,1), (5,8,1), (6,1,1), (7,7,1), (8,6,2), (9,3,5), (10,3,1), (11,3,2)]

def Programa():
    # Se inicializa la base de datos
    conn = sqlite3.connect('Libreria.sqlite3')
    conn.text_factory = unicode
    cur = conn.cursor()

    # Construcción y población de las tablas de la base de datos
    Creacion(cur)
    CompletarTablas(cur)

    # Ejecución de consultas
    PaisesCompras(cur)
    MediaCompradores(cur)
    Actualizar(cur, conn)
    MediaSoporte(cur)
    BorrarCompradores(cur, conn)

    #Se cierra el cursor y se actualiza la base de datos.
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
        CREATE TABLE Libros(
            registro INTEGER(4) PRIMARY KEY NOT NULL UNIQUE,
            titulo VARCHAR(35) NOT NULL DEFAULT '' UNIQUE,
            escritor VARCHAR(35) NOT NULL DEFAULT '',
            editorial VARCHAR(20) NOT NULL DEFAULT '',
            soporte VARCHAR(35) NOT NULL DEFAULT 'LIBRO',
            fecha_entrada DATE NOT NULL DEFAULT '0000-00-00' UNIQUE,
            pais VARCHAR(20) NOT NULL DEFAULT '',
            importe DECIMAL(8,2) NOT NULL DEFAULT 0.0,
            anotaciones BLOB
            )""")

    cur.execute(u"""
        CREATE TABLE Compradores(
            registro INTEGER(4) PRIMARY KEY NOT NULL UNIQUE,
            nombre VARCHAR(35) NOT NULL DEFAULT '',
            fecha_nacimiento DATE NOT NULL DEFAULT '0000-00-00',
            telefono VARCHAR(10) DEFAULT NULL,
            domicilio  VARCHAR(35) DEFAULT NULL,
            poblacion  VARCHAR(25) DEFAULT NULL,
            anotaciones  TEXT
            )""")

    cur.execute(u"""
        CREATE TABLE Compras(
            registro INTEGER(4) PRIMARY KEY NOT NULL UNIQUE,
            id_comprador INTEGER(4) NOT NULL DEFAULT '',
            id_libro INTEGER(4) NOT NULL DEFAULT ''
            )""")


def CompletarTablas(cur):
    cur.executemany(u"""
        INSERT INTO Libros (registro, titulo, escritor, editorial, soporte, fecha_entrada,pais,importe)
        VALUES ( ?, ?, ?, ? ,?, ? ,?, ?) """, listaInfoLibros)
    cur.executemany(u"""
        INSERT INTO Compradores (registro, nombre, fecha_nacimiento,telefono, domicilio,poblacion,anotaciones)
        VALUES ( ?, ?, ?, ?, ?, ? ,?) """,listaInfoCompradores)
    cur.executemany(u'INSERT INTO Compras (registro, id_comprador, id_libro) VALUES ( ?, ?, ?) ',listaInfoCompras)


################################################# Consultas ############################################################

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

    print u"País | Número de libros |"
    # Se imprimen los registros
    for tupla in query:
        for value in tupla:
            if type(value) == unicode:
                value.encode("utf-8")
            print value, "|",
        print

    print "=================================\n"

def MediaCompradores(cur):
    query = cur.execute(u"""
        SELECT poblacion, AVG(importe) AS media
        FROM Compradores c, Compras cl, Libros l
        WHERE c.registro = cl.id_comprador AND cl.id_libro = l.registro
        GROUP BY poblacion
        ORDER BY media DESC
        """)

    # Ahora se imprime con un poco de formato
    print u"Media de importes por población\n"

    print u"Población | Media |"
    for tupla in query:
        for value in tupla:
            if type(value) == unicode:
                value.encode("utf-8")
            elif type(value) == float:
                value = round(value, 2)
            print value, "|",
        print

    print "=================================\n"

def Actualizar(cur, conn):
    print u"Tabla de Compras antes de actualizar:\n"
    print u"(registro, id_comprador, id_libro)"
    query = cur.execute(u"""
        SELECT *
        FROM Compras
        """)

    for tupla in query:
        print tupla

    print "\n- - - - - - - - - - - - - - - -\n"

    cur.execute(u"UPDATE Compras set id_comprador=?, id_libro=? WHERE registro=?", [3,3,10])
    cur.execute(u"UPDATE Compras set id_comprador=?, id_libro=? WHERE registro=?", [3,7,11])
    conn.commit()

    print u"Tabla de Compras después de actualizar:\n"
    print u"(registro, id_comprador, id_libro)"
    query = cur.execute(u"""
        SELECT *
        FROM Compras
        """)

    for tupla in query:
        print tupla

    print "=================================\n"

def MediaSoporte(cur):
    query = cur.execute(u"""
        SELECT soporte, AVG(importe)
        FROM Libros
        GROUP BY soporte""")

    # Ahora se imprime con un poco de formato
    print u"Media de importes por soporte\n"

    print u"Soporte | Media |"
    for tupla in query:
        for value in tupla:
            if type(value) == unicode:
                value.encode("utf-8")
            elif type(value) == float:
                value = round(value, 2)
            print value, "|",
        print

    print "=================================\n"

def BorrarCompradores(cur, conn):
    print u"Tabla de Compradores antes de borrar:\n"
    print u"registro | nombre |"
    query = cur.execute(u"""
        SELECT registro, nombre
        FROM Compradores
        """)

    for tupla in query:
        for value in tupla:
            if type(value) == unicode:
                value.encode("utf-8")
            print value, "|",
        print

    print "\n- - - - - - - - - - - - - - - -\n"

    query = cur.execute(u"""
        DELETE FROM Compradores
        WHERE registro IN (
            SELECT registro
            FROM Compradores
            WHERE registro NOT IN (
                SELECT c.registro
                FROM Compradores c, Compras cl
                WHERE c.registro = cl.id_comprador
            )
        )
        """)
    conn.commit()

    for tupla in query:
        print tupla


    print u"Tabla de Compradores después de borrar:\n"
    print u"registro | nombre |"
    query = cur.execute(u"""
        SELECT registro, nombre
        FROM Compradores
        """)

    for tupla in query:
        for value in tupla:
            if type(value) == unicode:
                value.encode("utf-8")
            print value, "|",
        print

    print "=================================\n"

Programa()
