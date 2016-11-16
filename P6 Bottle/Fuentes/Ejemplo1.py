from bottle import route, run

@route('/hola')
def hola():
    return "<h1>Hola mundo</h1>"

run(host='localhost', port=8080, debug=True)
