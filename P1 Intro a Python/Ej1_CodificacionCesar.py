"""
    Practica 1 - Ejercicio 1
    
    Lorenzo de la Paz Suarez
    Juan Mas Aguilar
    Eli Emmanuel Linares Romero
    
    Lab 06 Puesto 01
    Gestion de la Informacion en la Web - 2016-2017
    Universidad Complutense de Madrid
    Madrid
    
"""

#Ejercicio 1


def cesar(txt,desplazarLetra,desplazarPalabra):
   
   texto =  desplazaLetra(txt, desplazarLetra)
   print ''.join(texto)
   texto = desplazaPalabras(texto, desplazarPalabra) 
   print texto
   
   
def desplazaLetra(txt, num):
    
    texto = []
    for i in range(0,len(txt)):
         if txt[i].isalpha():
            asciiNum = ord(txt[i])
            movimiento = num % 26
            nuevaPosicion = asciiNum + movimiento
            if asciiNum <= 90:
               if nuevaPosicion > 90:
                  nuevaPosicion = nuevaPosicion - 26
            else:
               if nuevaPosicion > 122:
                  nuevaPosicion = nuevaPosicion - 26
            texto.append(unichr(nuevaPosicion))
         else:
            texto.append(txt[i])
    
    return ''.join(texto)

def desplazaPalabras(txt, num):

   lista2 = []
   lista = txt.split()
   rotacion = num%len(lista)

   for  i in range(len(lista)):
      nuevaPosicion = i+rotacion
      if nuevaPosicion >= len(lista):
         nuevaPosicion = nuevaPosicion - len(lista)
      lista2.append(lista[nuevaPosicion] + " ")

   return  ''.join(lista2)    

     
   
    
    
    
    
