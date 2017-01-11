# -*- coding: utf-8 -*-

#
# CABECERA AQUI
#


from bottle import run, post
# Resto de importaciones
import hashlib
import binascii
from pymongo import MongoClient
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
    nickname = request.forms.get('nickname')
    name = request.forms.get('name')
    country = request.forms.get('country')
    email = request.forms.get('email')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')

    if contraseña != contraseñaRepetida:
        return template InfoView(info = "Las contraseñas no coinciden")
        
    doc = c.aggregate([ $match: { '_id': nick } ])
    
    if doc is not None:
        return template InfoView(info = "El alias de usuario ya existe")

    #insertar en la base de datos según nuestro criterio de almacenamiento
    chars = string.ascii_uppercase
    sal = ''.join(random.choice(chars) for _ in range(15))
    password += 'M'
    dk = hashlib.pbkdf2_hmac('sha256', password, sal, 100000)
    password = binascii.hexlify(dk)
    result = db.users.insert_one(
        {
            'nickname': nickname,
            'name': name,
            'country': country,
            'email': email,
            'password': password,
            'salt': sal,
            'it': 100000
        }
    #Devolvemos la página web
    return template View(nickName = nick)
    

@post('/change_password')
def change_password():
    nick = request.forms.get('nickname')
    contraseñaAntigua = request.forms.get('old_Password')
    contraseñaNueva = request.forms.get('new_Password')
    
    doc = c.aggregate([ $match: { '_id': nick },
                        $project: {'_id':0, 'salt':1}])
                        
    if doc is not None:
        sal = doc['salt']
    else:
        return template FailView(info = "Usuario incorrecto")

    password += 'M'
    dk = hashlib.pbkdf2_hmac('sha256', password, sal, 100000)
    contraseñaTransformada = binascii.hexlify(dk)
    
    doc = c.aggregate([ $match: { '_id': nick }, 
                        $match: { 'password': contraseñaTransformada } ])
    if doc is not None: #Alias no existe o si old_password no coincide con la contraseña almacenada:
        return template FailView(info = "Usuario o contraseña incorrectos")

    #Devolvemos la página web
    return template InfoView (info = "La contraseña del usuario ? ha sido modificada", nick)

@post('/login')
def login():
    nick = request.forms.get('nickname')
    contraseña = request.forms.get('password')
    
     doc = c.aggregate([ $match: { '_id': nick },
                        $project: {'_id':0, 'salt':1}])
                        
    if doc is not None:
        sal = doc['salt']
    else:
        return template FailView(info = "Usuario incorrecto")

    password += 'M'
    dk = hashlib.pbkdf2_hmac('sha256', password, sal, 100000)
    contraseñaTransformada = binascii.hexlify(dk)
    
    doc = c.aggregate([ $match: { '_id': nick }, 
                        $match: { 'password': contraseñaTransformada } ])
    if doc is not None: #Alias no existe o si password no coincide con la contraseña almacenada:
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
