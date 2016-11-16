# -*- coding: utf-8 -*-
# Practica 6 - Programacion Web

# Lorenzo de la Paz Suarez
# Juan Mas Aguilar
# Eli Emmanuel Linares Romero

# Lab 06 Puesto 01
# Gestion de la Informacion en la Web - 2016-2017
# Universidad Complutense de Madrid
# Madrid

import sqlite3

def Modelo():  
    #Usuarios    
    conn = sqlite3.connect(u"databases.sqlite3")
    conn.text_factory = unicode
    cur = conn.cursor()

    #Borramos si existe previamente la tabla
    cur.execute(u"DROP TABLE IF EXISTS Usuario")
    cur.execute(u"DROP TABLE IF EXISTS Contenidos")

    #Creamos las tablas
    cur.execute(u"""
        CREATE TABLE IF NOT EXISTS 'User' (
            user_id INTEGER AUTOINCREMET PRIMARY KEY NOT NULL,
            firstName VARCHAR(60) NOT NULL,
            lastName VARCHAR(60) NOT NULL,
            username VARCHAR(60) NOT NULL UNIQUE,
            password VARCHAR(60) NOT NULL,
            email VARCHAR(60) NOT NULL
            )""")

    cur.execute(u"""
        CREATE TABLE IF NOT EXISTS 'Contenidos' (
            registro INTEGER(4) AUTOINCREMET PRIMARY KEY NOT NULL UNIQUE,
            nameItem VARCHAR(35) NOT NULL DEFAULT '',
            ItemType VARCHAR(35) NOT NULL DEFAULT '',
            fecha_entrada DATE NOT NULL DEFAULT '0000-00-00' UNIQUE,
            numberOfItems INTEGER(4) NOT NULL DEFAULT 0,
            descripcion BLOB
            )""")
    cur.close()

    #Actualizamos el cursor
    conn.commit()

def dropTables(dn):
    # Se crea el cursor para ejecutar queries
    cur = db.cursor()

    cur.execute(u"DROP TABLE IF EXISTS User")

    # Se cierra el cursor y se actualiza la base de datos.
    cur.close()
    db.commit()

