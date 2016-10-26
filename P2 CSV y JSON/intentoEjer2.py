#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import operator

def Semaforo():

    #Abrimos los archivos
    try:
        archivo = open("semaforos.txt")
    except:
        print "No se ha podido abrir el fichero", "semaforos.txt"
        exit()


    #leemos el json
    aux = str(archivo.read())
    lista = json.loads(aux)

    totalSemaforos = 0

    dicSemaforos = dict()

    for i in range(len(lista["features"])):
        cadena = lista["features"][i]["properties"]["Description"]
        str_cadena = cadena.encode("utf-8")

        ubicacion_incompleta = str_cadena[str_cadena.find("Ubicación:</b>") +
            len("Ubicación:</b>"):]

        ubicacion = ubicacion_incompleta[:ubicacion_incompleta.find("<br />")]
        ubicacion = ubicacion.lstrip().rstrip()

        ocurrencias_incompleta =
            ubicacion_incompleta[ubicacion_incompleta.find("Semáforos:</b>") +
            len("Semáforos:</b>"):]
        ocurrencias =
            ocurrencias_incompleta[:ocurrencias_incompleta.find("<br />")]
        ocurrencias = ocurrencias.lstrip().rstrip()

        if ocurrencias == "":
            ocurrencias = 0
        else:
            ocurrencias = int(ocurrencias)

        if ubicacion in dicSemaforos:
            dicSemaforos[ubicacion] += ocurrencias
        else:
            dicSemaforos[ubicacion] = ocurrencias


    try:
        fichero_frecuencias = open('frecuenciaSemaforos.txt', 'w')
    except:
        print "No se ha podido generar el archivo de salida"
        exit()

    numTotalSemaforos = 0
    for clave in dicSemaforos:
        numTotalSemaforos += dicSemaforos[clave]

    for clave in dicSemaforos:
        fichero_frecuencias.write(clave + "\t\tFrecuencia: " +
            str(float(dicSemaforos[clave]) / float(numTotalSemaforos)) + "\n")

    fichero_frecuencias.close()

    # Guardo los 10 semáforos con más ocurrencias
    try:
        fsal2 = open('MayorFrecuenciaSemaforos.txt', 'w')
    except:
        print "No se ha podido generar el archivo de salida MayorFrecuencia"

    semaforos_ordenados = sorted(dicSemaforos.items(), key=lambda x:x[1])
    semaforos_ordenados = list(reversed(semaforos_ordenados))


    for semaforo in semaforos_ordenados[:10]:
        fsal2.write(semaforo[0] + "\t\tOcurrencias: " + str(semaforo[1]) + "\n")

    fsal2.close()

Semaforo()
