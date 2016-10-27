#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
import urllib

#ERRORES: NO DETECTA LOS MONUMENTOS CON TILDES O Ñ



def descripcion(url):
    
    contenido = urllib.urlopen(url)
    parser = contenido.find("body")
    parser = parser.find("div\div\div\div")
    parser = parser.findall("div")
    parser = parser[1].findall("div")
    parser = parser[1].find("main")
    parser = parser.findall("div")
    parser = parser[3].find("div\div\div")
    parser = parser.findall("div")
    parser = parser[1].findall("p")

    while

    print descripcion
    
def Monumentos ():

    #Abrimos el archivo y lo parseamos
    entrada = open("MonumentosZaragoza.xml", "rt")
    arbol = ElementTree.parse(entrada);
    
    #Guardamos todos los monumentos en una lista
    listaNombres = []
    for nodo in arbol.findall('Feature'):
        nombre = nodo.find('PropertyValue').text
        listaNombres.append(nombre.encode("utf-8"))

    #print listaNombres

    #Le pedimos la usuario el monumento
    print "De que documento quiere obtener informacion?"
    monumento = raw_input()
    
    if(monumento in listaNombres):
       # url = url()
        descripcion("http://www.zaragoza.es/ciudad/vistasciudad/detalle_Monumento?id=66")
       # longitud, latitud =  longLat()
       
       # print "Nombre del monumento: " + monumento + '\n'
       # print "Latitud: " + latitud + "  Longitud: " + longitud + '\n'
       # print "Página web asociada:\n" + url + '\n'
       # print "Descripción:\n" + descripcion
    else:
        print "No existe ese monumento"








    
Monumentos()
