#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.etree import ElementTree
from xml.dom import minidom
import re
import urllib

#Clase Monumeto que guarda la informacion del monumento con un método que lo imprime
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
        print "Pagina web asociada:"
        print "\t" + self.url + "\n"
        print "Descripcion:\n"
        print self.descripcion


def main():

    monumentos(abrirArchivo());

def abrirArchivo():

    
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

    #Lo guardamos en una lista de monumentos
    for feature in arbol.iter("Feature"):
        propertyValues = list(feature)
        nuevoMonumento = Monumento()
        for pValue in propertyValues:
            if pValue.attrib["name"] == "nombre":
                nuevoMonumento.nombre = pValue.text
            elif pValue.attrib["name"] == "url":
                nuevoMonumento.url = pValue.text
        lstMonumentos.append(nuevoMonumento)

    return lstMonumentos

def monumentos(lstMonumentos):

    #Imprimimos los monumentos
    imprimirMonumentos(lstMonumentos)

    #Recogemos la respuesta
    indiceMonumento = raw_input("Introduzca el numero del monumento para ver su informacion:\n")

    #Comprobamos que es un numero entero
    try:
        indiceMonumento = int(indiceMonumento) - 1
    except:
        print "No se introdujo un numero.\n"
        exit()

    #Comprobamos que el monumento existe
    while indiceMonumento < 0 or indiceMonumento >= len(lstMonumentos):
        print "No existe un monumento con ese numero. Vuelva a intentarlo.\n"

        indiceMonumento = raw_input("Introduzca el numero del monumento para ver su informacion:\n")

        try:
            indiceMonumento = int(indiceMonumento) - 1
        except:
            print "No se introdujo un numero.\n"
            exit()

    #Si la descripcion está vacia hay que analizar el monumento
    if lstMonumentos[indiceMonumento].descripcion == "":
        lstMonumentos[indiceMonumento] = analizarMonumento(lstMonumentos[indiceMonumento])

    #imprime el monumento
    lstMonumentos[indiceMonumento].imprimir()

    #Si el usuario quiere ver otro, hacemos una llamada recursiva
    respuesta = raw_input("\nDesea ver otro monumento?(s/n)")

    if (respuesta == "s"):
        monumentos(lstMonumentos)

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

    #Cortamos lo que no sirve
    headerDescp = u"<h3>Descripción</h3>"

    data = data[data.find(headerDescp) + len(headerDescp):]
    data = data[:data.find(u"</div>")]

    #limpiamos el texto de etiquetas xml
    cleantext = cleanxml(data)
    monumento.descripcion = cleantext

    return monumento


#Funcion que limpia las etiquetas xml
def cleanxml(raw_xml):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_xml)

  if(cleantext.find(u"Más Datos") >= 0):
      cleantext = cleantext[:cleantext.find(u"Más Datos")]

  return cleantext



main()
