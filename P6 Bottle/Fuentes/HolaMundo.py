from bottle import route, run

@route('/hola')
def hola():
    return "<h1>¡Hola Mundo!</h1>"

run(host='0.0.0.0', port=8080)
