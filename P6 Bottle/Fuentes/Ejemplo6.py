from bottle import Bottle,route,run,request,template
@route('/dict')
def dict():
    datos={"Nombre":"Maria","Telefono":689933456}
    return template('template_dict.tpl',dict=datos)
run(host='0.0.0.0', port=8080)
