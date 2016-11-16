# -*- coding: utf-8 -*-
# Practica 6 - Programacion Web

# Lorenzo de la Paz Suarez
# Juan Mas Aguilar
# Eli Emmanuel Linares Romero

# Lab 06 Puesto 01
# Gestion de la Informacion en la Web - 2016-2017
# Universidad Complutense de Madrid
# Madrid
# Controlador



import sqlite3
from bottle import rute, run, templates

@route('/login')
def login():
    output = template('loginView.tpl')    
    return output


@route('/login', method='POST')
def do_logIn():

    username = request.forms.get('user')
    password = request.forms.get('password')
    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor();
    #Comprobamos en la base de datos 
    cur.execute(u"SELECT username AS user, password AS pass FROM User WHERE User.username =?. User.password =?", [username, password])
    if (len(cur.fetchall()) == 0):
        return template("loginIncorrectView.tpl")
    #else:
        #return template("main.tpl")

    
@route('/signup')
def signUp():
    output = template('registerView.tpl')
    return output

    
@route('/signup', method='POST')
def do_signUp():

    firstname = request.forms.get('firstname')
    lastname = request.forms.get('lastaname')
    username = request.forms.get('user')
    password = request.forms.get('password')
    re_password = request.forms.get('confirm_password')

    #comprobamos que las contraseñas son iguales
    if password != re_password: return template("registerAgainView.tpl")

    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor();
    
    #Si lo son, comprobamos que el usuario no existe
    cur.execute(u"SELECT username AS user FROM User WHERE User.username =?", [username])
    if (len(cur.fetchall()) > 0): return template("registerAgainView.tpl")

    return template("registrationSuccessfulView.tpl")
    


run(host='0.0.0.0',  port=8080)
