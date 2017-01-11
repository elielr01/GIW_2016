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
    nick = request.forms.get('nick')
    nombre = request.forms.get('nombre')
    pais = request.forms.get('pais')
    correo = request.forms.get('correo')
    contraseña = request.forms.get('contraseña')
    contraseñaRepetida = request.forms.get('contraseñaRepetida')

    if contraseña != contraseñaRepetida:
        return template InfoView(info = "Las contraseñas no coinciden")
        
    doc = c.aggregate([ $match: { '_id': nick } ])
    
    if doc is not None:
        return template InfoView(info = "El alias de usuario ya existe")

    #insertar en la base de datos según nuestro criterio de almacenamiento
    seed = 
    #Devolvemos la página web
    return template View(nickName = nick)
    

@post('/change_password')
def change_password():
    nick = request.forms.get('nick')
    contraseñaAntigua = request.forms.get('oldPassword')
    contraseñaNueva = request.forms.get('newPassword')
    
    #Transformacion de contraseña
    #contraseñaTransformada = ... 
    #############################
    
    doc = c.aggregate([ $match: { '_id': nick }, 
                        $match: { 'password': contraseñaTransformada } ])
    if doc is not None: #Alias no existe o si old_password no coincide con la contraseña almacenada:
        return template FailView(info = "Usuario o contraseña incorrectos")

    #Devolvemos la página web
    return template InfoView (info = "La contraseña del usuario ? ha sido modificada", nick)

@post('/login')
def login():
    nick = request.forms.get('nick')
    contraseña = request.forms.get('contraseña')
    
    #Transformacion de contraseña
    #contraseñaTransformada = ... 
    #############################
    
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
