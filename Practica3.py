#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.etree import ElementTree
import urllib

#-----------ERRORES: 1-UTF-8 como siempre jaja. 2- Hay que coger solo una latitud y una longitud


def Monumentos():

    #Abrimos el archivo
    try: 
        arch = open("MonumentosZaragoza.xml", "rt")
    except:
        print "No se ha podido abrir el archivo MonumentosZaragoza.xml"

    #lo convertimos en arbol
    arbol = ElementTree.parse(arch)
    
    print "Monumentos: "

    #recorremos y los vamos mostrando al usuario
    for nodo in arbol.iter("{http://idezar.unizar.es/SimpleXML}PropertyValue"):
        if nodo.attrib.get('name') == 'nombre':
            print nodo.text

    #Pedimos monumento
    monumento = raw_input("Elige un monumento: ")

    #Recorremos el arbol (FIJARSE ALGORITMO)
    parse = False
    for nodo in arbol.iter():
        if(nodo.attrib.get('name') == 'url' and parse == True):
            url = nodo.text
            break;
        if nodo.attrib.get('name') == 'nombre' and nodo.text == monumento:
            parse = True

    #traza
    print "URL:   ", url

    #Nos vamos a la web
    contenido = urllib.urlopen(url)
    #print contenido.read()
    #description = contenido.read().encode("utf-8")
    #aux = "<h3>Descripción</h3>"
    #aux = aux.encode("utf-8")
    #aux2 = "<h3>Enlaces</h3>"
    #aux2 = aux2.encode("utf-8")
    #description = description.split(aux)[1].split()[0].split(aux2)[0]
    #print description

#---------------Parte B-------------------
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
    urlGoogle = serviceurl + urllib.urlencode({'address': monumento,'components':'country:ES'})
    uh= urllib.urlopen(urlGoogle)
    arbolito = ElementTree.parse(uh)

    for nodo in arbolito.iter():
        if nodo.tag == 'lat':
            latitud = nodo.text
        if nodo.tag == 'lng':
            longitud = nodo.text

    print "------------TEXTO FINAL FORMATEADO:---------------"
    print "Nombre monumento:  ", monumento
    print "Latitud: ",latitud," Longitud: ",longitud
    print "Página web asociada: ", url
    print "Descripción: ", description
    
Monumentos()

