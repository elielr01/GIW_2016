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
    dropTables()

    #Usuarios
    conn = sqlite3.connect(u"database.sqlite3")
    conn.text_factory = unicode
    cur = conn.cursor()

    #Creamos las tablas
    cur.execute(u"""
        CREATE TABLE IF NOT EXISTS 'User' (
            user_id INTEGER PRIMARY KEY,
            firstName VARCHAR(60) NOT NULL,
            lastName VARCHAR(60) NOT NULL,
            username VARCHAR(60) NOT NULL UNIQUE,
            password VARCHAR(60) NOT NULL,
            email VARCHAR(60) NOT NULL
            )""")

    cur.execute(u"""
        CREATE TABLE IF NOT EXISTS 'Contenidos' (
            registro INTEGER PRIMARY KEY,
            nameItem VARCHAR(35) NOT NULL DEFAULT '' UNIQUE,
            itemType VARCHAR(35) NOT NULL DEFAULT '',
            fecha_entrada DATE NOT NULL DEFAULT '0000-00-00' UNIQUE,
            numberOfItems INTEGER(4) NOT NULL DEFAULT 0,
            descripcion BLOB
            )""")
    cur.close()

    #Actualizamos el cursor
    conn.commit()

def dropTables():

    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor()


    # Se crea el cursor para ejecutar queries
    cur = db.cursor()

    cur.execute(u"DROP TABLE IF EXISTS User")
    cur.execute(u"DROP TABLE IF EXISTS Contenidos")

    # Se cierra el cursor y se actualiza la base de datos.
    cur.close()
    db.commit()

Modelo()
