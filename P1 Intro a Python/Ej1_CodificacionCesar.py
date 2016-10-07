# -*- coding: utf-8 -*-
"""
    Práctica 1 - Ejercicio 1

    Lorenzo de la Paz Suarez
    Juan Mas Aguilar
    Elí Emmanuel Linares Romero

    Lab 06 Puesto 01
    Gestion de la Información en la Web - 2016-2017
    Universidad Complutense de Madrid
    Madrid

"""

#Ejercicio 1


def cesar(txt,desplazarLetra,desplazarPalabra):

   texto =  desplazaLetra(txt, desplazarLetra)
  # txt = desplazaPalabras(txt, desplazarPalabra)
   print texto


def desplazaLetra(txt, num):

    texto = " "
    for i in range(0, len(txt)):
        if txt[i].isalpha():
            if txt[i] == 'x' or txt[i] == 'y' or txt[i] == 'z' or txt[i] == 'X' or txt[i] == 'Y' or txt[i] == 'Z':
                - (26 - num)
            else:
                  texto[i] = txt[i] + num

            print txt[i]
