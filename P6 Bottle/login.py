# -*- coding: utf-8 -*-
from bottle import *
from BeautifulSoup import *

@route('/login')
def login():
    return template('loginView')

@post('/login')
def do_login():
    return template('loginIncorrectView')

@route('/signUp')
def comida():
    return template('registerView')

@post('/signUp')
def simon():
    return template('registrationSuccessfulView')



run(host='0.0.0.0', port = 8080)
