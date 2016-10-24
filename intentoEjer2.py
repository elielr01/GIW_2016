#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

#PROBLEMAS: ASCII CODE, NO ME LEE EN UTF-8.

def Semaforo():

    #Abrimos los archivos
    try:
        archivo = open("semaforos.txt")
    except:
        print "No se ha podido abrir el fichero", "semaforos.txt"
        exit()
    try:
        fsal = open('frecuenciaSemaforos.txt', 'w')
    except:
        print "No se ha podido generar el archivo de salida"
        exit()

    #recogemos lo leído
    aux = str(archivo.read())
    lista = json.loads(aux)
    i = 0
    diccionario = dict()

    #print json.dumps(lista, indent=4) #Para usar si lo quereis ver mejor
    totalSemaforos = 0
    
    for i in range(len(lista["features"])):   
        #print json.dumps(lista["features"][i]["properties"]["Description"], indent=4)  #si quieres ver elformato
        cadena = lista["features"][i]["properties"]["Description"]
        
        numberOfSemaforos = int(cadena.split('</b>')[2].split('<br')[0].strip())
        place = cadena.split('</b>')[3].split('\n')[0]
        ubicacion = cadena.split('</b>')[1].split('<br')[0].strip()
        
        diccionario[cadena.split('</b>')[1].split('<br')[0]] = numberOfSemaforos
        #print "Ubicacion: ",ubicacion,"Numero de semaforos: ", numberOfSemaforos,"Se encuentra en: ", place
        totalSemaforos += numberOfSemaforos

    for clave in diccionario:
        num = float(diccionario[clave])/float(totalSemaforos)
        try:
            fsal.write(clave + "," + str(num) + '\n')
        except:
            hola = 5;
    fsal.close()
    try:
        fsal2 = open('MayorFrecuenciaSemaforos.txt', 'w')
    except:
        print "No se ha podido generar el archivo de salida MayorFrecuencia"  

    # a continuacion, algoritmo para almacenar los menores
    i = 0
    lista = []
    menor = i
    for linea in diccionario:
        if len(lista) <= 10:
            lista.append(linea)
            if(diccionario[linea] < lista[menor]):
                menor = len(lista) - 1
        elif(diccionario[linea] < lista[menor]):
            lista[menor] = linea
    
    #recorremos la lista y vamos guardando
    for linea in lista:
        try:
            
            fsal2.write([linea + " "+ str(diccionario[linea]) + '\n'])
        except:
            hola = 2;
    fsal2.close()
    
Semaforo()
        
