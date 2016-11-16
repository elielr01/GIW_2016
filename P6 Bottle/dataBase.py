# -*- coding: utf-8 -*-
import sqlite3


def main():
    # Se inicializa la base de datos
    db = sqlite3.connect(u"inventory.sqlite3")
    db.text_factory = unicode

    # Se crean tablas
    createsDataBase(db)

    # Se eliminan las tablas (para propósitos de debugging)
    #dropTables(db)

    # Se actualiza la base de datos.
    db.commit()

def createsDataBase(db):
    # Se crea el cursor para ejecutar queries
    cur = db.cursor()

    cur.execute(u"""
        CREATE TABLE IF NOT EXISTS 'User' (
            user_id INTEGER AUTOINCREMET PRIMARY KEY NOT NULL,
            firstName VARCHAR(60) NOT NULL,
            lastName VARCHAR(60) NOT NULL,
            username VARCHAR(60) NOT NULL,
            password VARCHAR(60) NOT NULL
            )""")
    cur.execute(u"""
        CREATE TABLE IF NOT EXISTS 'Content' (
            content_id INTEGER AUTOINCREMET PRIMARY KEY NOT NULL,
            name VARCHAR(60) NOT NULL,
            description VARCHAR(60) NOT NULL,
            category VARCHAR(60) NOT NULL
            )""")



    # Se cierra el cursor y se actualiza la base de datos.
    cur.close()
    db.commit()

def dropTables(dn):
    # Se crea el cursor para ejecutar queries
    cur = db.cursor()

    cur.execute(u"DROP TABLE IF EXISTS User")

    # Se cierra el cursor y se actualiza la base de datos.
    cur.close()
    db.commit()

main()
