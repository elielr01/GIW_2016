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
c = db['usuarios']

@get('/top_countries')
# http://localhost:8080/top_countries?n=3
def agg1():

    numPaises = request.query.n
    pass


@get('/products')
# http://localhost:8080/products?min=2.34
def agg2():

    minPrice = request.query.min
    pass

    
@get('/age_range')
# http://localhost:8080/age_range?min=80
def agg3():

    minUsers = request.query.min
    pass
    
    
@get('/avg_lines')
# http://localhost:8080/avg_lines
def agg4():
    pass
    
    
@get('/total_country')
# http://localhost:8080/total_country?c=Alemania
def agg5():

    nameCountry = request.query.c
    pass
    
        
if __name__ == "__main__":
    # No cambiar host ni port ni debug
    run(host='localhost',port=8080,debug=True)
