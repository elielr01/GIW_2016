from bottle import Bottle,route,run,request
@route('/login') 
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="usuario" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>'''

@route('/login',method='POST') 
def do_login():
    username = request.forms.get('usuario')
    password = request.forms.get('password')
    if username=="antonio" and password=="antonio":
        return "<p>Login correcto</p>"
    else:
        return "<p>Login incorrecto.</p>"

run(host='localhost', port=8080)
