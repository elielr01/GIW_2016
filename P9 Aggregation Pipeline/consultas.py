# -*- coding: utf-8 -*-
# Practica 9 - Aggregation Pipeline

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
# Aggregation Pipeline
from pymongo import MongoClient
from bottle import *

mongoclient = MongoClient()
db = mongoclient['giw']

@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():

    c = db['usuarios']
    numPaises = request.query.n

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "n" or int(numPaises) < 1:
            invalid_arguments.append(parameter)

    #Si hay argumentos inválidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_View.tpl', invalid_arguments = invalid_arguments,tipo="Users")

    #Tubería de agregación
    doc = c.aggregate([{'$group': {'_id':'$pais','sum_users':{'$sum': 1}} },
                       {'$sort': {'sum_users':-1}},
                       {'$limit': int(numPaises)}
                       ])

    if(doc is not None):
        return template('Find_View.tpl',data=doc,ejercicio=1)
    else:
        return template('Find_Fail_View.tpl',tipo="Users",fail=doc)

@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():


    c = db['pedidos']

    minPrice = request.query.min

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "min" or float(minPrice) <= 0:
            invalid_arguments.append(parameter)

    #Si hay argumentos inválidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_View.tpl', invalid_arguments = invalid_arguments,tipo="Order Items")

    cursor = c.aggregate([{'$unwind': '$lineas'},
                          {'$match' : {'lineas.precio':{'$gte':float(minPrice)} } },
                          {'$group': {'_id': '$lineas.nombre', 'cantidadTotal': {'$sum': '$lineas.cantidad'},
                                      'precio': {'$first': '$lineas.precio'}}}
                          ])
    if(cursor is None):
        return template("Find_Fail__View.tpl", tipo="Order Items",fail = minPrice)
    else:
        return template("Find_View.tpl", data = cursor, ejercicio=2)

@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():

    c = db['usuarios']
    minUsers = request.query.min

    #Se revisa que todos los argumentos sean válidos
    invalid_arguments = []
    for parameter in request.query:
        if parameter != "min" or int(minUsers) < 0:
            invalid_arguments.append(parameter)

    #Si hay argumentos inválidos se regresa una vista que lo indique
    if len(invalid_arguments) > 0:
        return template('Invalid_Find_View.tpl', invalid_arguments = invalid_arguments,tipo="Users")

    #Falta aqui tubería
    doc = c.aggregate( [ {'$group': {'_id':'$pais', 'numUsers': {'$sum':1}, 'minEdad': {'$min':'$edad'} , 'maxEdad': {'$max':'$edad'} }  },
                        {'$match': {'numUsers': {'$gte':int(minUsers)} }  },
                        {'$project': {'rangoEdades': {'$concat':[{'$substr': ['$minEdad',0,1]},'-',{'$substr': ['$maxEdad',0,3]}]},'numUsers':1}},
                         {'$sort': {'rangoEdades':-1,'_id':1} }
        ])
    if(doc is not None):
        return template('Find_View.tpl',data=doc,ejercicio=3)
    else:
        return template('Find_Fail_View.tpl',tipo="Users",fail=doc)

@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():

    c = db['usuarios']
    doc = c.aggregate([{'$lookup':
                            {
                              'from': 'pedidos',
                              'localField' : '_id',
                              'foreignField': 'cliente',
                              'as' : 'pedidosPorCliente'
                            }
                       },
                       {'$group':
                            {
                                '_id':'$pais',
                                'sumPedidos':{'$sum': 1}
                            }
                       },
                       {'$project':
                            {
                                'mediaPedidos':{'$avg':'$sumPedidos'}
                            }
                       }
    ])

    if(doc is not None):
        return template('Find_View.tpl',data=doc,ejercicio=4)
    else:
        return template('Find_Fail_View.tpl',tipo="Average Lines",fail=doc)

    pass


@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():

    nameCountry = request.query.c
    pass


if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
