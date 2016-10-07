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

    texto = desplazaPalabras(texto, desplazarPalabra) 
    print texto
   
   
def desplazaLetra(txt, num):
"""En la siguiente función desplazamos las letras de un texto 'txt'
    'num' veces según el abecedario.
Observando la tabla ascii, hemos podido resolver el ejercicio"""    
    texto = []
    for i in range(0,len(txt)):
        #Si es una letra
         if txt[i].isalpha():
                
             #obtenemos el número en código ascii
            asciiNum = ord(txt[i])
            
            #obtenemos el movimiento. Usamos el módulo por si el usuario
            #pone un nº mayor que 26, el nº de letras del abecedario
            movimiento = num % 26
            nuevaPosicion = asciiNum + movimiento
            
            #Comprobamos si es una letra mayúsculas
            if asciiNum <= 90:
                #Si se excede la nueva posición del rango de las letras
               if nuevaPosicion > 90:
                  nuevaPosicion = nuevaPosicion - 26
                    
            else:   #Si se excede la nueva posición del rango de las letras
               if nuevaPosicion > 122:
                  nuevaPosicion = nuevaPosicion - 26
                    
            #añadimos la nueva letra
            texto.append(unichr(nuevaPosicion))
           #si no es una letra la añadimos igualmente
         else:
            texto.append(txt[i])
            
    #devolvemos un string en vez de una lista
    return ''.join(texto)

def desplazaPalabras(txt, num):
"""En la siguiente función desplazamos las palabras de un texto 'txt', 'num' veces.
    Hemos usado dos listas y un diccionario. 
                    """
   lista2 = []
    #separamos el texto y lo introducimos en una lista
   lista = txt.split()
   
    #calculamos la rotación.Usamos el módulo para abarcar el caso 
    #en el que el desplazamiento 'num' es mayor que el número de palabras 
   rotacion = num % len(lista)

   for  i in range(len(lista)):
        
        #calculamos la nueva posición
      nuevaPosicion = i + rotacion
    
        #si se excede de la longitud de la lista, calculamos la verdadera
      if nuevaPosicion >= len(lista):
         nuevaPosicion = nuevaPosicion - len(lista)
            
        #añadimos siempre a 'lista2'
      lista2.append(lista[nuevaPosicion] + " ")

    #convertimos a un string la lista
   return  ''.join(lista2)    

     
   
    
    
    
    
