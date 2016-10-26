# -*- coding: utf-8 -*-

import json

def Semaforo():

    # se abre el archivo que contiene el json
    try:
        archivo = open("semaforos.txt")
    except:
        print "No se ha podido abrir el fichero", "semaforos.txt"
        exit()

    # se lee el json
    aux = str(archivo.read())
    lista = json.loads(aux)

    dicSemaforos = dict()

    for i in range(len(lista["features"])):

        # se obtiene el xml en string de los atributos del semáforo
        cadena = lista["features"][i]["properties"]["Description"]
        str_cadena = cadena.encode("utf-8")

        # se obtiene la ubicación del semáforo
        ubicacion_incompleta = str_cadena[str_cadena.find("Ubicación:</b>") +
            len("Ubicación:</b>"):]

        ubicacion = ubicacion_incompleta[:ubicacion_incompleta.find("<br />")]
        ubicacion = ubicacion.lstrip().rstrip()

        # se obtiene el número de ocurrencias para esa instancia de semáforo
        ocurrencias_incompleta = ubicacion_incompleta[ubicacion_incompleta.find("Semáforos:</b>") +
            len("Semáforos:</b>"):]
        ocurrencias = ocurrencias_incompleta[:ocurrencias_incompleta.find("<br />")]
        ocurrencias = ocurrencias.lstrip().rstrip()

        # se convierte a un dato de tipo Int las ocurrencias
        if ocurrencias == "":
            ocurrencias = 0
        else:
            ocurrencias = int(ocurrencias)

        # Si el semáforo ya fue registrado, se le suma a sus ocurrencias
        # Si no está registrado, simplemente se agrega al diccionario.
        if ubicacion in dicSemaforos:
            dicSemaforos[ubicacion] += ocurrencias
        else:
            dicSemaforos[ubicacion] = ocurrencias

    # Ahora se guarda la frecuencia de cada semáforo en un archivo.
    try:
        fichero_frecuencias = open('frecuenciaSemaforos.txt', 'w')
    except:
        print "No se ha podido generar el archivo de salida"
        exit()

    # Se suma el número total de ocurrencias de todos los semáforos
    numTotalSemaforos = 0
    for clave in dicSemaforos:
        numTotalSemaforos += dicSemaforos[clave]

    # Ya con el número total de ocurrencias, se imprimen las frecuencias
    for clave in dicSemaforos:
        fichero_frecuencias.write(clave + "\t\tFrecuencia: " +
            str(float(dicSemaforos[clave]) / float(numTotalSemaforos)) + "\n")

    fichero_frecuencias.close()

    # Ahora se guardan los 10 semáforos con más frecuencias en otro archivo
    try:
        fsal2 = open('MayorFrecuenciaSemaforos.txt', 'w')
    except:
        print "No se ha podido generar el archivo de salida MayorFrecuencia"

    # Se crea una lista de tuplas del diccionario, ordenando los semáforos
    # a partir de su número de ocurrencias de mayor a menor.
    semaforos_ordenados = sorted(dicSemaforos.items(), key=lambda x:x[1])
    semaforos_ordenados = list(reversed(semaforos_ordenados))

    # Se imprimen los primeros 10 de la lista de semáforos creada.
    for semaforo in semaforos_ordenados[:10]:
        fsal2.write(semaforo[0] + "\t\tOcurrencias: " + str(semaforo[1]) + "\n")

    fsal2.close()

Semaforo()
