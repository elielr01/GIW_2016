# -*- coding: utf-8 -*-
# Practica 10 - Autenticación & TOTP

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
# Autenticación & TOTP
from bottle import run, post
from pymongo import MongoClient


##############
# APARTADO 1 #
##############

# 
# Explicación detallada del mecanismo escogido para el almacenamiento de c
# contraseñas, explicando razonadamente por qué es seguro
#

mongoclient = MongoClient()
db = mongoclient['giw']
c = db['users']

@post('/signup')
def signup():
    nick = request.query.nickname
    nombre = request.query.name
    pais = request.query.country
    correo = request.query.email
    contraseña = request.query.password
    contraseñaRepetida = request.query.password2

    if contraseña != contraseñaRepetida:
        return template InfoView(info = "Las contraseñas no coinciden")
    if True:
        return template InfoView(info = "El alias de usuario ya existe")

    #insertar en la base de datos según nuestro criterio de almancenamiento

    #Devolvemos la página web
    return template View(nickName = nick)
    

@post('/change_password')
def change_password():
    nick = request.query.nickname
    contraseñaAntigua = request.query.old_password
    contraseñaNueva = request.query.new_password

    if #Alias no existe o si old_password no coincide con la contraseña almacenada:
        return template FailView(info = "Usuario o contraseña incorrectos")

    #Devolvemos la página web
    return template InfoView (info = "La contraseña del usuario ? ha sido modificada", nick)

@post('/login')
def login():
    nick = request.query.nickname
    contraseña = request.query.password

    if #Alias no existe o si password no coincide con la contraseña almacenada:
        return template FailView(info = "Usuario o contraseña incorrectos")

    #Devolvemos la página web
    return template View(nickName = nick)


##############
# APARTADO 2 #
##############


def gen_secret():
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    pass
    
    
def gen_gauth_url(app_name, username, secret):
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    pass
        

def gen_qrcode_url(gauth_url):
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    pass
    


@post('/signup_totp')
def signup_totp():
    pass
        
        
@post('/login_totp')        
def login_totp():
    pass

    
if __name__ == "__main__":
    # NO MODIFICAR LOS PARÁMETROS DE run()
    run(host='localhost',port=8080,debug=True)
