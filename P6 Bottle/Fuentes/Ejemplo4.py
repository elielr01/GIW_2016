from bottle import Bottle,route,run,request,template
@route('/hola')
@route('/hola/')
@route('/hola/<nombre1>')
def hola(nombre1='Mundo'):
    return template('template_hola.tpl', nombre=nombre1)
run(host='0.0.0.0', port=8080)
