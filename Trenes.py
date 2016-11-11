import urllib
from BeautifulSoup import *


#-------------------------Main-------------------------

def Main():
    RecogerImagenesWebs()
    MiniBuscador()
#-------------------------1º Programa-------------------------
def RecogerImagenesWebs():
    html = urllib.urlopen('http://trenesytiempos.blogspot.com.es/').read()
    sopa = BeautifulSoup(html)
    etiquetas = sopa('a')
    print "-----Vamos a acceder a las entradas de 2016-----"
    print "---------------Para sacar sus imagenes---------------"
    print "------------------------------------------------------------------"

    #Variables para ir acumulando
    contador = 0
    j=0
    #recorremos las etiquetas
    for et in etiquetas:
        try:
            if "http://trenesytiempos.blogspot.com.es/2016_" in et.get('href',None):
                    contador+=1
                    print "Pagina web: ",et.get('href',None)
                    html2 = urllib.urlopen(et.get('href',None)).read()
                    soup = BeautifulSoup(html2)
                    etiquetas=soup('a',{"imageanchor":"1"})
                    for etiquet in etiquetas:
                        
                        archivo2=open("foto"+str(j)+".jpg","wb")
                        imagen=urllib.urlopen(etiquet.get('href',None))
                        while True:
                            info = imagen.read(100000)
                            if len(info) < 1 : break
                            archivo2.write(info)
                            archivo2.close()
                            j=j+1 
        except:
            hol1=6
            
        hola=8
        
    #Printear      
    print "Hay ",contador,"  webs"
    print "Hay ",j, " fotos"

#-------------------------2º Programa-------------------------

def MiniBuscador():

    #Cogemos las palabras clave
    claves = []
    palabra = raw_input("Introduzca las palabras clave (Intro entre cada una). 0 para salir")
    
    while(palabra != 0):
        claves.append(palabra)
        palabra = raw_input("Introduzca las palabras clave (Intro entre cada una). 0 para salir")

    #buscamos las palabras
    html = urrlib.urlopen('http://trenesytiempos.blogspot.com.es/')
    sopa = BeautifulSoup(html)
    
    for palabra in claves    
        print "Entradas con " + palabra
        for entrada in sopa.findAll(text=palabra)
            #al no poder guardar, creo que esto solo imprimiria la palabra (faltaria poder sacar la url de la entrada que contiene esa palabra y eliminar duplicados)
            print entrada
        


#Llamada
Main()
