# -*- coding: utf-8 -*-
# Practica 10 - Autenticacion y TOTP

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
# Aggregation Pipeline

from bottle import *
# Resto de importaciones
import hashlib
import binascii
import random
from pymongo import MongoClient
# APARTADO 1 #
##############

#
# Explicación detallada del mecanismo escogido para el almacenamiento de
# contraseñas, explicando razonadamente por qué es seguro
#
# Para esta práctica hemos utilizado una función que implementa un standard de criptografía de clave pública
# especificamente conocida como PKCS #5 v2.0. Esta función implementa un algoritmo hash indicado (en nuestro caso
# SHA-256, con una sal, un número de iteraciones determinados (función de realentización, en nuestro caso 100000) y la
# contraseña a la que previamente le añadimos la pimienta incrustada en el código(M). El hash permite evitar la
# exposición directa de la contraseña o el descifrado de la misma, la sal disminuye las probabilidades de éxito de un
# ataque con tablas rainbow y la pimienta y función de realentización hacen poco viable la ruptura por fuerza bruta.

mongoclient = MongoClient()
db = mongoclient['giw']
c = db['users']

SAL_GENERATOR = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PIMIENTA = 'nuwhf4FHXMD3FHdHsUeQwe39uUrMXf82FhaE13F'
ITERACIONES_HASH = 100000

@post('/signup')
def signup():
    nickname = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')


    if db.users.find({'_id': nickname}).count() > 0:
            return template('InfoView.tpl', title = "Error", info = "El alias de usuario ya existe")

    if password != password2:
        return template('InfoView.tpl', title = "Error", info = "Las contraseñas no coinciden")

    #comprobaciones
    if (nickname == '' or password == ''):
        return template('InfoView.tpl', title = "Error", info = "Currate un poco el/la usuario/contraseña ;)")

    #insertar en la base de datos según nuestro criterio de almacenamiento

    #Se crea una sal
    sal = ''.join(random.choice(SAL_GENERATOR) for _ in range(64))

    #Se le agrega la pimienta
    password += PIMIENTA

    #Se aplica función hash
    dk = hashlib.pbkdf2_hmac('sha256', password, sal, ITERACIONES_HASH)
    password = binascii.hexlify(dk)

    result = db.users.insert_one(
        {
            '_id': nickname,
            'name': name,
            'country': country,
            'email': email,
            'password': password,
            'salt': sal
        })
    #Devolvemos la página web
    return template('InfoView.tpl', title = "Bienvenido", info = "Bienvenido usuario " + name)



@post('/change_password')
def change_password():
    nick = request.forms.get('nickname')
    contrasenaAntigua = request.forms.get('old_password')
    contrasenaNueva = request.forms.get('new_password')

    cur = db.users.find({'_id': nick})

    if cur.count() != 1 or nick == '' or contrasenaAntigua == '':
        return template('InfoView.tpl', title = "Error", info = "Usuario o contraseña incorrectos")
    
    #Se verifica que la contraseña antigua sea la correcta

    #Se obtiene la sal original del usuario
    for doc in cur:
        salUsuario = str(doc['salt'])

    #Se agrega la pimienta
    contrasenaAntigua += PIMIENTA

    #Se aplica la función hash
    dk = hashlib.pbkdf2_hmac('sha256', contrasenaAntigua, salUsuario, ITERACIONES_HASH)
    contrasenaAntiguaTransformada = binascii.hexlify(dk)

    if contrasenaAntiguaTransformada != doc['password']:
        return template('InfoView.tpl', title = "Error", info = "Usuario o contraseña incorrectos")

    #Si el alias existe y la contraseña es correcta, entonces se cambia la contraseña.
    #Se crea una sal
    salNueva = ''.join(random.choice(SAL_GENERATOR) for _ in range(64))

    #Se le agrega la pimienta
    contrasenaNueva += PIMIENTA

    #Se aplica función hash
    dk = hashlib.pbkdf2_hmac('sha256', contrasenaNueva, salNueva, ITERACIONES_HASH)
    contrasenaNueva = binascii.hexlify(dk)

    #Se modifica en la base de datos
    result = db.users.update_one({'_id': nick}, {'$set': {'password':contrasenaNueva, 'salt': salNueva}})

    #Devolvemos la página web
    return template('InfoView.tpl', title = "Cambio de contraseña exitoso",
                    info = "La contraseña del usuario " + nick + " ha sido modificada")

@post('/login')
def login():
    nick = request.forms.get('nickname')
    contrasena = request.forms.get('password')

    cur = db.users.find({'_id': nick})

    if cur.count() != 1:
        return template('InfoView.tpl', title = "Error", info = "Usuario o contraseña incorrectos")

    #Se verifica que la contraseña sea la correcta

    #Se obtiene la sal original del usuario
    for doc in cur:
        sal = str(doc['salt'])
        name = doc['name']

    #Se agrega la pimienta
    contrasena += PIMIENTA

    #Se aplica la función hash
    dk = hashlib.pbkdf2_hmac('sha256', contrasena, sal, ITERACIONES_HASH)
    contrasena = binascii.hexlify(dk)

    if contrasena != doc['password']:
        return template('InfoView.tpl', title = "Error", info = "Usuario o contraseña incorrectos")

    #Devolvemos la página web
    return template('InfoView.tpl', title = "Bienvenido", info = "Bienvenido " + name)


##############
# APARTADO 2 #
##############


def gen_secret():
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    GENERATOR = "234567ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    seed = ''.join(random.choice(SAL_GENERATOR) for _ in range(32))
    return seed[:15]

def gen_gauth_url(app_name, username, secret):
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    return 'otpauth://totp/'+username+'?secret='+secret+'&issuer='+app_name


def gen_qrcode_url(gauth_url):
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    pass



@post('/signup_totp')
def signup_totp():

    nickname = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')


    if db.users.find({'_id': nickname}).count() > 0:
            return template('InfoView.tpl', title = "Error", info = "El alias de usuario ya existe")

    if password != password2:
        return template('InfoView.tpl', title = "Error", info = "Las contraseñas no coinciden")

    #comprobaciones
    if (nickname == '' or password == ''):
        return template('InfoView.tpl', title = "Error", info = "Currate un poco el/la usuario/contraseña ;)")

    #Falta AQUI todo el tema de totp


   #Devolvemos la página web
    return template('InfoView.tpl', title = "Bienvenido", info = "Bienvenido usuario " + name)

@post('/login_totp')
def login_totp():

    nick = request.forms.get('nickname')
    contrasena = request.forms.get('password')
    totp = request.forms.get('totp')

    cur = db.users.find({'_id': nick})

    if cur.count() != 1:
        return template('InfoView.tpl', title = "Error", info = "Usuario o contraseña incorrectos")

    #Falta aqui todo el tema del totp

   #Devolvemos la página web
    return template('InfoView.tpl', title = "Bienvenido", info = "Bienvenido " + name)


if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
