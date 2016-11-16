from bottle import route, run

@route('/')
@route('/hola/<nombre>')
def saludo(nombre='Pepito'):
    return 'Hola %s, bienvenid@'%nombre

run(host='localhost', port=8080, debug=True)
