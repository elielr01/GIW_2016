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

'''
Pasos para probarlo (By Lorenzo jeje):
1- Ir a la web https://console.developers.google.com/
2- Crear proyecto y habilitar el API de google+
3-Generar creenciales OAth, creando: client_id,secret y redirect_uri
4-Modificar el CLIENT_ID y el CLIENT_SECRET de tu aplicación (cada cuenta de cada uno será distinto)
'''

#Creo que la función está ya hecha
@get('/login_google')
def login_google():
    jsonurl = urllib.urlopen(DISCOVERY_DOC).read()
    urlj = json.loads(str(jsonurl))
    tipo = 'email'
    url = urlj['authorization_endpoint']+'?client_id='+CLIENT_ID+'&response_type=code&scope=openid%20'+tipo+'&redirect_uri='+REDIRECT_URI
    return template('loginGoogle.tpl',url = url)

@get('/token')
def token():

    #Obtengo el código temporal
    codigo = request.query.code
    
    #Obtengo el json 
    jsonurl = urllib.urlopen(DISCOVERY_DOC).read()
    urlj = json.loads(str(jsonurl))

    #envio un POST a google y me lo devuelve como json- NO FUNCIONA
    urlPedirToken = urllib.urlopen(TOKEN_VALIDATION_ENDPOINT+'?code='+codigo+'&secret='+CLIENT_SECRET).read()
    jsonToken = json.loads(str(urlPedirToken))

    #Falta aqui descifrar la contrasena y el usuario
    
    #Devolvemos la página web de bienvenida
    return template('WelcomeView.tpl',email=mail)


if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
