# -*- coding: utf-8 -*-

# Practica 10 - Autenticación delegada

#Juan Mas Aguilar, Lorenzo De La Paz Suárez y Eli Emmanuel Linares Romero declaramos que esta solución
#es fruto exclusivamente nuestro trabajo personal. No hemos sido
#ayudados por ninguna otra persona ni hemos obtenido la solución de
#fuentes externas, y tampoco hemos compartido nuestra solución con
#nadie. Declaramos además que no hemos realizado de manera deshonesta
#ninguna otra actividad que pueda mejorar nuestros resultados
#ni perjudicar los resultados de los demás.

# Lab 06 Puesto 01
# Gestion de la Informacion en la Web - 2016-2017
# Universidad Complutense de Madrid
# Madrid
# Autenticación delegada
from bottle import run, get, template, request
# Resto de importaciones
import urllib
import json
import hashlib
import random
import os
import bottle

from beaker.middleware import SessionMiddleware

# Credenciales.
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
# Copiar los valores adecuados.
CLIENT_ID     = '103910203478-dafoffk6mkl6ib02l1btse6ec4mc3lrc.apps.googleusercontent.com'
CLIENT_SECRET = 'XzcIMgyOukKi7XyJbjP1EjxA'
REDIRECT_URI  = "http://localhost:8080/token"

# Fichero de descubrimiento para obtener el 'authorization endpoint' y el
# 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"


# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKEN_VALIDATION_ENDPOINT = "https://www.googleapis.com/oauth2/v4/token"

URL = urllib.urlopen(DISCOVERY_DOC).read()
JSONURL = json.loads(str(URL))

#Creo que la función está ya hecha
@get('/login_google')
def login_google():

    session = bottle.request.environ.get('beaker.session')
    session['state'] = hashlib.sha256(os.urandom(1024)).hexdigest()
    session.save()

    tipo = 'email'
    url = (JSONURL['authorization_endpoint'] + '?client_id=' + CLIENT_ID + '&response_type=code&scope=' +
        urllib.quote('openid ', safe = '')+ tipo + '&redirect_uri=' + REDIRECT_URI + '&state=' +
        session['state'])

    return template('loginGoogle.tpl',url = url)

@get('/token')
def token():

    #Obtengo el código temporal
    codigo = request.query.code

    session = bottle.request.environ.get('beaker.session')

    #Comprobamos que el state
    if(request.query.state !=  session['state']):
        return template('FailView.tpl')

    #envio un POST a google y me lo devuelve como json
    data = urllib.urlencode({'code':codigo,'client_id':CLIENT_ID,'client_secret':CLIENT_SECRET,'redirect_uri':REDIRECT_URI,'grant_type':'authorization_code'})
    urlPedirToken = urllib.urlopen(JSONURL['token_endpoint'],data).read()
    jsonToken = json.loads(str(urlPedirToken))

    #Falta aqui descifrar la contrasena y el usuario
    id_token = jsonToken['id_token']

    #envio un POST a google y me lo devuelve como json
    data = urllib.urlencode({'id_token':id_token})
    jsonDecodificado = urllib.urlopen('https://www.googleapis.com/oauth2/v3/tokeninfo',data).read()
    jsonToken = json.loads(str(jsonDecodificado))

    #Obtenemos el email
    mail = jsonToken['email']

    #del SESSIONS[request.query.state]
    #Devolvemos la página web de bienvenida
    return template('WelcomeView.tpl',email=mail)


if __name__ == "__main__":

    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './data',
        'session.auto': True
    }
    app = SessionMiddleware(bottle.app(), session_opts)

    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(app=app, host='localhost',port=8080,debug=True)
