import urllib
import os
import re

from BeautifulSoup import *

#-------------------------Main--------------------------------

def Main():
    
    RecogerImagenesWebs()
    Buscador()
#-------------------------1º Programa-------------------------
def RecogerImagenesWebs():
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    sopa = BeautifulSoup(html)
    etiquetas = sopa('a')
    print "-----Vamos a acceder a las entradas de 2016-----"
    print "---------------Para sacar sus imagenes---------------"
    print "------------Guardando las imagenes en carpetas...-----------"

    #guardo mi dirección dónde se encuentra el archivo
    place = os.getcwd()
    #Variables para ir acumulando
    contador = 0
    j,k=0,0
    
    #recorremos las etiquetas
    for et in etiquetas:
        try:
            web = et.get('href',None)
            if "http://trenesytiempos.blogspot.com.es/2016_" in web:

                    #crea la carpeta y me introduzco en ella
                    os.makedirs("Carpeta"+str(contador))
                    os.chdir("Carpeta"+str(contador))
                    print "------------Creamos la carpeta ",str(contador),"...-----------"
                    #Nos conectamos a la web
                    html2 = urllib.urlopen(web).read()
                    soup = BeautifulSoup(html2)
                    etiquetasL=soup('a',{"imageanchor":"1"})

                    #Recorremos el conjunto de las imagenes
                    for etiquet in etiquetasL:
                        
                        #Creo la imagen y guardo sus datos
                        archivo2=open("foto"+str(j)+".jpg","wb")
                        imagen=urllib.urlopen(etiquet.get('href',None))
                        while True:
                            info = imagen.read(100000)
                            if len(info) < 1 : break
                            archivo2.write(info)
                        archivo2.close()
                        j=j+1
                    #Incremento el contador
                    contador+=1
                    os.chdir(place)
        except:
            dummy=0
        
    #Printear      
    print "Hay ",contador,"  webs"
    print "Hay ",j, " fotos"

#-------------------------2º Programa-------------------------
def Buscador():
    print "------------------------------------------------------------------"
    
    #Pedimos al usuario las palabras clave
    palabra = raw_input("Introduzca un conjunto de palabras clave para buscarlas: ")
    print "--------------------------Wait a few seconds...-------------------"
    listaPalabras = palabra.split()
    diccionario = dict()
    
    #Nos conectamos a la web
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    sopa = BeautifulSoup(html)
    etiquetas = sopa('a')
    
    #recorremos
    for et in etiquetas:   
        try:
            #comprobamos que es una entrada valida
            web = et.get('href',None)
            
            if "http://trenesytiempos.blogspot.com.es/201" in web and web[42] == '_':
                htmlAux = urllib.urlopen(web).read()
                sopaAux = BeautifulSoup(htmlAux)

                #recorremos la lista de palabras para ver si está en la web
                for pal in listaPalabras:
                    
                    #vemos si esta la palabra 'pal'
                    if sopaAux.find(text=re.compile(pal)):
                        
                        #La añadimos a la lista de la clave del diccionario
                        if pal in diccionario:
                            diccionario[pal].append(web)
                        else:
                            diccionario[pal] = []
                            diccionario[pal].append(web)
                        
        except:
            dummy=0
            
    #Vamos a mostrar los resultados
    print "------------------------------------------------------------------"
    print "Resultados:"

    #recorremos el diccionario y vamos mostrando las palabras clave junto con sus webs
    for clave in diccionario:
        print "Palabra clave: ",clave
        
        #Exists or not
        if len(diccionario[clave]) > 0:
            print "Encontrada en las siguientes webs:"
        else:
            print "No se ha encontrado en ninguna web."
            continue  
        for url in diccionario[clave]:
            print url
        print "-  -   -   -   -   -   -   -    -   -    -    -   -"


        
#Llamada
Main()
