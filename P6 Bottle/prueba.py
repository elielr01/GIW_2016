# -*- coding: utf-8 -*-
from bottle import *
from BeautifulSoup import *

@route('/hola')

def hola():
    return "<h1>Hello World!</h1>"

run(host='0.0.0.0', port = 8080)
