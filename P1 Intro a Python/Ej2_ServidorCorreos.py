# -*- coding: utf-8 -*-
"""
    Práctica 1 - Ejercicio 2

    Lorenzo de la Paz Suarez
    Juan Mas Aguilar
    Elí Emmanuel Linares Romero

    Lab 06 Puesto 01
    Gestion de la Información en la Web - 2016-2017
    Universidad Complutense de Madrid
    Madrid

"""


# Ejercicio 2
# Este ejercicio fue probado con el servidor gratuito de Google: smtp.gmail.com:587
# Para esto se necesita tener una cuenta en gmail con la seguridad de acceso a la cuenta
#

from smtplib import SMTP

def correoE():
    nombreServer = raw_input("Introduce el nombre del servidor (Ej. smtp.gmail.com): \n")
    numeroPuerto = raw_input("Introduzca el numero del puerto (Ej. 587): \n")

    #Capturar servidor
    servidor = SMTP(nombreServer, numeroPuerto)
    servidor.ehlo()
    servidor.starttls()
    servidor.ehlo()

    #Para que funcione se necesita desactivar la seguridad de acceso a la cuenta
    #Activacion de acceso para aplicaciones menos seguras
    username = raw_input("Introduce tu usuario:\n")
    password = raw_input("Introduce tu contraseña:\n")

    servidor.login(username, password)
    #Mientras no recibamos confirmación de que debemos salir, no hacemos nada
    comprobar = False
    while comprobar == False:
       comprobar = enviar(servidor, username)

    servidor.quit()

def enviar(servidor, username):
    enviado = False

    #Capturar destinatario
    nombreDestinatario = raw_input("Introduce el correo del destinatario: \n")

    #Capturar mensaje
    mensaje = raw_input("Introduce el mensaje:\n ")

    #Si quiere enviar el mensaje
    if(raw_input("¿Quiere enviar el mensaje? ") == "Si"):

        #controlamos excepciones y mandamos el correo
        try:
            servidor.sendmail(username, nombreDestinatario, mensaje)
            print "Mensaje enviado correctamente"
        except:
            print "Error. No se ha podido enviar el mensaje"

        enviado = True
        #si quieres enviar otro mensaje
    elif (raw_input("¿Quiere enviar otro mensaje? ") != "Si"):
        enviado = True

    return enviado

correoE()
