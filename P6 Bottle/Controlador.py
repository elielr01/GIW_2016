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
from bottle import *
from BeautifulSoup import *

app = Bottle()

@app.route('/')
@app.route('/login')
def login():
    return template('loginView.tpl')


@app.route('/login', method='POST')
def do_logIn():

    username = request.forms.get('user')
    password = request.forms.get('password')
    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor();
    #Comprobamos en la base de datos
    query = cur.execute(u"SELECT * FROM User WHERE username =? AND password =?", [username, password])

    if (len(query.fetchall()) == 0):
        cur.close()
        return template("loginIncorrectView.tpl")
    else:
        query = cur.execute(u"SELECT user_id, firstName FROM User WHERE username =? AND password =?", [username, password])
        for row in query:
            user_id = row[0]
            name = row[1]
        cur.close()
        return template('loginSuccessfulView.tpl', id=user_id, name=name)


@app.route('/signUp')
def signUp():
    return template('registerView.tpl')


@app.route('/signUp', method='POST')
def do_signUp():

    firstname = request.forms.get('firstName')
    lastname = request.forms.get('lastName')
    username = request.forms.get('username')
    password = request.forms.get('password')
    re_password = request.forms.get('confirm_password')
    email = request.forms.get('email')
    re_email = request.forms.get('confirm_email')

    #comprobamos que las contraseñas y correos son iguales
    if (password != re_password or email != re_email or firstname == '' or lastname == '' or
        username == '' or password == '' or email == ''):
        return template("registerAgainView.tpl")


    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor();

    #Si lo son, comprobamos que el usuario no existe
    query = cur.execute(u"SELECT username FROM User WHERE username =?", [username])
    if (len(query.fetchall()) > 0):
        cur.close()
        return template("registerAgainView.tpl")

    #Si no existe se agrega
    cur.execute(u"""
        INSERT INTO User (firstName, lastName, username, password, email)
        VALUES(?,?,?,?,?)""",
        [firstname, lastname, username, password, email])

    cur.close()
    db.commit()
    return template("registrationSuccessfulView.tpl")

@app.route('/index')
def index():
    user_id = request.query.id
    user_name = request.query.name
    return template('index.tpl',id=user_id, name = user_name)

@app.post('/index')
def index_post():
    user_id = request.forms.get('id')
    user_name = request.forms.get('name')
    return template('index.tpl',id=user_id, name = user_name)

@app.route('/inventory')
def inventory():
    user_id = request.query.id
    user_name = request.query.name

    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor()

    data = cur.execute(u"""
        SELECT *
        FROM Contenidos
                       """)

    return template('showInventoryView',id=user_id, name = user_name, data=data)

@app.route('/search')
def search():
    user_id = request.query.id
    user_name = request.query.name
    return template('searchItemView.tpl',id=user_id, name = user_name)

@app.route('/add')
def add():
    user_id = request.query.id
    user_name = request.query.name
    return template('addItemView.tpl',id=user_id, name = user_name)

@app.post('/add')
def add():
    user_id = request.forms.get('id')
    user_name = request.forms.get('name')

    itemName = request.forms.get('itemName')
    itemCategory = request.forms.get('itemCategory')
    quantity = request.forms.get('quantity')
    description = request.forms.get('description')
    date = datetime.now()

    # Si algún campo NOT NULL está vacío se pregunta de nuevo el item
    if (itemName == '' or itemCategory == '' or quantity == ''):
        return template('addItemIncorrectView.tpl', id=user_id, name=user_name)

    # Si todo está bien, se realiza la inserción
    db = sqlite3.connect(u"database.sqlite3")
    cur = db.cursor()

    cur.execute(u"""
        INSERT INTO Contenidos (nameItem, ItemType, fecha_entrada, numberOfItems, descripcion)
        VALUES (?,?,?, ?, ?)""",
        [itemName, itemCategory, date, quantity, description])

    cur.close()
    db.commit()
    return template('addItemSuccessful.tpl', id=user_id, name=user_name)

@app.route('/delete')
def delete():
    user_id = request.query.id
    user_name = request.query.name
    return template('deleteItemView.tpl',id=user_id, name = user_name)

@app.route('/modify')
def modify():
    user_id = request.query.id
    user_name = request.query.name
    return template('modifyItemView.tpl',id=user_id, name = user_name)



app.run(host='0.0.0.0',  port=8080)
