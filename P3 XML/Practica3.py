#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.etree import ElementTree
from xml.dom import minidom
import urllib

#-----------ERRORES: 1-UTF-8 como siempre jaja. 2- Hay que coger solo una latitud y una longitud

class Monumento:

    def __init__(self):
        self.nombre = ""
        self.url = ""
        self.latitud = ""
        self.longitud = ""
        self.descripcion = ""

    def imprimir(self):
        print "Nombre del monumento: " + self.nombre
        print "Latitud: " + self.latitud + " Longitud: " + self.longitud
        print "Página web asociada:"
        print "\t" + self.url
        print "Descripción:"
        print self.descripcion




def imprimirMonumentos(lstMonumentos):
    i = 1
    for monumento in lstMonumentos:
        print str(i) + ". " + monumento.nombre
        i += 1

def analizarMonumento(monumento):

    monumento.nombre = monumento.nombre.encode("utf-8")

    #Primero obtenemos latitud y longitud
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
    url = serviceurl + urllib.urlencode({'address': monumento.nombre,'components':'country:ES'})
    uh = urllib.urlopen(url)

    arbol = ElementTree.parse(uh)
    for nodo in arbol.iter("location"):
        monumento.latitud = nodo.find("lat").text
        monumento.longitud = nodo.find("lng").text

    #Despues conseguimos la descripcion
    contenido = urllib.urlopen(monumento.url)

    data = contenido.read().decode("latin1")

    headerDescp = u"<h3>Descripción</h3>"
    footDescp = u"<h3>Enlaces</h3>"
    print data
    raw_input()
    print "\n\n\n\n\n\n"

    data = data[data.find(headerDescp) + len(headerDescp):]
    print "Lo que sobra despues de substr es:\n" + data
    raw_input()

    print "\n\n\n\n\n\n"

    try:
        from BeautifulSoup import BeautifulSoup
    except ImportError:
        from bs4 import BeautifulSoup

    parsed_html = BeautifulSoup(data)

    data = data[:data.find(footDescp)]
    print "Al final:\n" + data
    raw_input()


    return monumento

def Monumentos():

    #Abrimos el archivo
    try:
        arch = open("MonumentosZaragoza.xml", "rt")
    except:
        print "No se ha podido abrir el archivo MonumentosZaragoza.xml"
        exit()

    #lo convertimos en arbol
    arbol = ElementTree.parse(arch)

    print "Monumentos: "

    lstMonumentos = []

    i = 1
    for feature in arbol.iter("Feature"):
        propertyValues = list(feature)
        nuevoMonumento = Monumento()
        for pValue in propertyValues:
            if pValue.attrib["name"] == "nombre":
                nuevoMonumento.nombre = pValue.text
                print str(i) + ". " + nuevoMonumento.nombre
                i += 1
            elif pValue.attrib["name"] == "url":
                nuevoMonumento.url = pValue.text
        lstMonumentos.append(nuevoMonumento)


    indiceMonumento = raw_input("Introduzca el número del monumento para ver su información:\n")

    try:
        indiceMonumento = int(indiceMonumento) - 1
    except:
        print "No se introdujo un número.\n"
        exit()

    while indiceMonumento < 0 or indiceMonumento >= len(lstMonumentos):
        print "No existe un monumento con ese número. Vuelva a intentarlo.\n"

        indiceMonumento = raw_input("Introduzca el número del monumento para ver su información:\n")

        try:
            indiceMonumento = int(indiceMonumento) - 1
        except:
            print "No se introdujo un número.\n"
            exit()

    if lstMonumentos[indiceMonumento].descripcion == "":
        lstMonumentos[indiceMonumento] = analizarMonumento(lstMonumentos[indiceMonumento])

    lstMonumentos[indiceMonumento].imprimir()

    respuesta = raw_input("¿Desea ver otro monumento?(s/n)")

    while respuesta == "s":

        imprimirMonumentos(lstMonumentos)

        indiceMonumento = raw_input("Introduzca el número del monumento para ver su información:\n")

        try:
            indiceMonumento = int(indiceMonumento) - 1
        except:
            print "No se introdujo un número.\n"
            exit()

        while indiceMonumento < 0 or indiceMonumento >= len(lstMonumentos):
            print "No existe un monumento con ese número. Vuelva a intentarlo.\n"

            indiceMonumento = raw_input("Introduzca el número del monumento para ver su información:\n")

            try:
                indiceMonumento = int(indiceMonumento) - 1
            except:
                print "No se introdujo un número.\n"
                exit()

        if lstMonumentos[indiceMonumento].descripcion == "":
            lstMonumentos[indiceMonumento] = analizarMonumento(lstMonumentos[indiceMonumento])

        lstMonumentos[indiceMonumento].imprimir()

        respuesta = raw_input("¿Desea ver otro monumento?(s/n)")

    """
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
    """


def prettifyXML():

    strXML = minidom.parse("MonumentosZaragoza.xml")
    pretty_xml_as_string = strXML.toprettyxml()

    print pretty_xml_as_string
    raw_input()
    print "\n\n"



Monumentos()
#prettifyXML()
