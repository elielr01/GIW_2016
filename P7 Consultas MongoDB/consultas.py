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

mongoclient = MongoClient()
db = mongoclient['giw']
c = db['usuarios']

@get('/find_user')
def find_user():
    # http://localhost:8080/find_user?username=burgoscarla

    #recojo el username
    user_name = request.query.username

    #encuentro el primer usuario con ese username
    doc = c.find_one({'_id':user_name})

    #dependiendo de si existe el usuario
    if(doc is not None):
        return template('Find_User_View.tpl', doc=doc)
    else:
        return template('Fail_Find_User_View.tpl', user_name = user_name)


@get('/find_users')
def find_users():
    # http://localhost:8080/find_users?name=Luz
    # http://localhost:8080/find_users?name=Luz&surname=Romero
    # http://localhost:8080/find_users?name=Luz&food=hotdog

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "name" and parameter != "surname" and parameter != "birthday":
            invalid_arguments.append(parameter)


    #Si hay argumentos invalidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_Users_View.tpl', invalid_arguments = invalid_arguments)


    #Recojo los parametros de la url
    nombre = request.query.name
    apellido = request.query.surname
    cumpleanos = request.query.birthday

    # 2^3 posibilidades con los tres parametros
    if len(nombre) == 0 and len(apellido) ==0 and len(cumpleanos) == 0 :
        users = c.find({"name":nombre})

    elif len(nombre) == 0 and len(apellido) !=0 and len(cumpleanos) != 0:
        users = c.find({"surname":apellido, "birthdate":cumpleanos})

    elif len(nombre) != 0 and len(apellido) ==0 and len(cumpleanos) == 0:
        users = c.find({"name":nombre})

    elif len(nombre) == 0 and len(apellido) !=0 and len(cumpleanos) == 0:
        users = c.find({"surname":apellido})

    elif len(nombre) == 0 and len(apellido) ==0 and len(cumpleanos) != 0:
        users = c.find({"birthdate":cumpleanos})

    elif len(nombre) != 0 and len(apellido) ==0 and len(cumpleanos) != 0:
        users = c.find({"name":nombre,"birthdate":cumpleanos})

    elif len(nombre) != 0 and len(apellido) !=0 and len(cumpleanos) == 0:

        users = c.find({"name":nombre,"surname":apellido})
    else:
        users = c.find({"name":nombre,"surname":apellido,"birthdate":cumpleanos})
    print type(users)
    return template('Find_Users_View.tpl', data=users)


@get('/find_users_or')
def find_users_or():
    # http://localhost:8080/find_users_or?name=Luz&surname=Corral

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "name" and parameter != "surname" and parameter != "birthday":
            invalid_arguments.append(parameter)


    #Si hay argumentos invalidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_Users_View.tpl', invalid_arguments = invalid_arguments)

    #Recojo los parametros de la url
    nombre = request.query.name
    apellido = request.query.surname
    cumpleanos = request.query.birthday

    # 2^3 posibilidades con los tres parametros
    if len(nombre) == 0 and len(apellido) ==0 and len(cumpleanos) == 0 :
        users = c.find({"name":nombre})

    elif len(nombre) == 0 and len(apellido) !=0 and len(cumpleanos) != 0:
        users = c.find({ "$or": [{"surname":apellido},{"birthdate":cumpleanos}] } )

    elif len(nombre) != 0 and len(apellido) ==0 and len(cumpleanos) == 0:
        users = c.find({"name":nombre})

    elif len(nombre) == 0 and len(apellido) !=0 and len(cumpleanos) == 0:
        users = c.find({"surname":apellido})

    elif len(nombre) == 0 and len(apellido) ==0 and len(cumpleanos) != 0:
        users = c.find({"birthdate":cumpleanos})

    elif len(nombre) != 0 and len(apellido) ==0 and len(cumpleanos) != 0:
        users = c.find( { "$or": [{"name":nombre},{"birthdate":cumpleanos}] } )

    elif len(nombre) != 0 and len(apellido) !=0 and len(cumpleanos) == 0:
        users = c.find({ "$or" : [{"name":nombre},{"surname":apellido} ] } )

    else:
        users = c.find({ "$or" : [{"name":nombre},{"surname":apellido},{"birthdate":cumpleanos}] })

    return template('Find_Users_View.tpl', data=users)

@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "like":
            invalid_arguments.append(parameter)


    #Si hay argumentos invalidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_Users_View.tpl', invalid_arguments = invalid_arguments)

    #recojo el gusto
    gusto = request.query.like

    #encuentro el primer usuario con ese username
    users = c.find({"likes":gusto})

    return template('Find_Users_View.tpl',data=users)

@get('/find_country')
def find_country():
    # http://localhost:8080/find_country?country=Irlanda

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "country":
            invalid_arguments.append(parameter)


    #Si hay argumentos invalidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_Users_View.tpl', invalid_arguments = invalid_arguments)

    #recojo el country
    pais = request.query.country

    #encuentro el primer usuario con ese country
    users = c.find({"address.country":pais})

    return template('Find_Users_View.tpl',data=users)


@get('/find_email_birthdate')
def email_birthdate():
    # http://localhost:8080/find_email_birthdate?from=1973-01-01&to=1990-12-31

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "from" and parameter != "to":
            invalid_arguments.append(parameter)


    #Si hay argumentos invalidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0 or len(request.query) == 0:
        return template('Invalid_Find_Users_View.tpl', invalid_arguments = invalid_arguments)

    #Se obtienen los parametros
    from_date = request.query["from"]
    to_date = request.query.to

    users = c.find({"birthdate":{"$gte":from_date, "$lte":to_date}}).sort([("birthdate", 1), ("_id", 1)])

    return template('Find_Email_Birthdate.tpl',data=users)


@get('/find_country_likes_limit_sorted')
def find_country_likes_limit_sorted():
    # http://localhost:8080/find_country_likes_limit_sorted?country=Irlanda&likes=movies,animals&limit=4&ord=asc

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "country" and parameter != "likes" and parameter != "limit" and parameter != "ord":
            invalid_arguments.append(parameter)


    #Si hay argumentos invalidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0 or len(request.query) == 0:
        return template('Invalid_Find_Users_View.tpl', invalid_arguments = invalid_arguments)

    #Se obtienen los parametros
    country = request.query.country
    likes = request.query.likes.split(",")
    limit = int(request.query.limit)

    ord_str = request.query.ord
    if ord_str == "asc":
        order = 1
    else:
        order = -1

    users = c.find({"likes":{"$in":likes}, "address.country":country}).sort("birthdate", order).limit(limit)

    return template('Find_Users_View.tpl',data=users)


if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
