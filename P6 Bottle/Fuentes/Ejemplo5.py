from bottle import Bottle,route,run,request,template
@route('/suma/<num1>/<num2>')
def suma(num1,num2):
    return template('template_suma.tpl',numero1=num1,numero2=num2)
run(host='0.0.0.0', port=8080)
