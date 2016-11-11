import urllib
from BeautifulSoup import *


#-------------------------Main-------------------------

def Main():
    RecogerImagenesWebs()
    
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




#Llamada
Main()
