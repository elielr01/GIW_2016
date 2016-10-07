# -*- coding: utf-8 -*-
"""
    Práctica 1 - Ejercicio 3

    Lorenzo de la Paz Suarez
    Juan Mas Aguilar
    Elí Emmanuel Linares Romero

    Lab 06 Puesto 01
    Gestion de la Información en la Web - 2016-2017
    Universidad Complutense de Madrid
    Madrid

"""


# Ejercicio 3

def contarPalabrasDeArchivo():
    nombreArchivoEntrada = raw_input("Introduzca el nombre del archivo que quiere leer:\n")

    # Se intenta abrir el fichero
    try:
        manf = open(nombreArchivoEntrada)
    except:
        print "No se ha podido abrir el archivo: ", nombreArchivoEntrada
        exit()

    # Si el fichero es correcto, se lee.
    dicPalabras = dict()    # Este diccionario guardará las palabras y la cantidad de veces que aparece
    for linea in manf:
        linea = linea.rstrip()

        lststrPalabras = linea.split()
        for i in range(0, len(lststrPalabras)):
            # Si la palabra ya exste en el diccionario, se le suma 1 ocurrencia
            if lststrPalabras[i] in dicPalabras:
                dicPalabras[lststrPalabras[i]] = dicPalabras[lststrPalabras[i]] + 1
            # Si no, se agrega al diccionario
            else:
                dicPalabras[lststrPalabras[i]] = 1

    # Se escribe las palabras y sus ocurrencias en un fichero de salida.
    fsal = open('palabras.txt', 'w')

    for clave in dicPalabras:
        fsal.write(str(clave) + ' ' + str(dicPalabras[clave]) + '\n')

    fsal.close()
    manf.close()

contarPalabrasDeArchivo()
