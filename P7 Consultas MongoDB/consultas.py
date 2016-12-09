# -*- coding: utf-8 -*-
# Practica 7 - Consultas MongoDB

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
# Consultas MongoDB 
from pymongo import MongoClient
from bottle import *

@get('/find_user')
def find_user():
    # http://localhost:8080/find_user?username=burgoscarla
    mongoclient = MongoClient()
    db = mongoclient['giw']
    c = db['usuarios']
    user_name = request.query.username
    doc = c.find_one({'_id':user_name})
    if(doc is not None):    
        return template('Find_User_View.tpl', doc=doc)
    else:
        return template('Fail_Find_User_View.tpl', user_name = user_name)


@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&food=hotdog
    mongoclient = MongoClient()
    db = mongoclient['giw']
    c = db['usuarios']
    nombre = request.query.name
    apellido = request.query.surname
    cumpleanos = request.query.birthday
    if len(nombre) == 0 and len(apellido) ==0 and len(cumpleanos) == 0 :
        return template('Fail_Find_Users_View.tpl', user_name = "Not user ")
    elif len(nombre) == 0 and len(apellido) !=0 and len(cumpleanos) != 0:
        users = c.find({"surname":apellido, "birthdate":cumpleanos})
        print "Traza1"
    elif len(nombre) != 0 and len(apellido) ==0 and len(cumpleanos) == 0:
        users = c.find({"name":nombre})
        print "Traza2"
    elif len(nombre) == 0 and len(apellido) !=0 and len(cumpleanos) == 0:
        users = c.find({"surname":apellido})
        print "Traza3"
    elif len(nombre) == 0 and len(apellido) ==0 and len(cumpleanos) != 0:
        users = c.find({"birthdate":cumpleanos})
        print "Traza4"
    elif len(nombre) != 0 and len(apellido) ==0 and len(cumpleanos) != 0:
        users = c.find({"name":nombre,"birthdate":cumpleanos})
        print "Traza5"
    elif len(nombre) != 0 and len(apellido) !=0 and len(cumpleanos) == 0:
        print "Traza6"
        users = c.find({"name":nombre,"surname":apellido}) 
    else:
        users = c.find({"name":nombre,"surname":apellido,"birthdate":cumpleanos})
        print "Traza7"
        
    if(users is not None):    
        return template('Find_Users_View.tpl', data=users)
    else:
        return template('Fail_Find_Users_View.tpl', user_name = nombre)
        
        
@get('/find_users_or')
def find_users_or():
    # http://localhost:8080/find_users_or?name=Luz&surname=Corral
    pass
       
               
@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football
    pass


@get('/find_country')
def find_country():
    # http://localhost:8080/find_country?country=Irlanda
    pass
    
    
@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31
    pass
    
    
@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc
    pass

    
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
