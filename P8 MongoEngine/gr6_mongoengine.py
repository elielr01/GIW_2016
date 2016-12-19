# -*- coding: utf-8 -*-
# Practica 8 - MongoEngine

#Juan Mas Aguilar, Lorenzo De La Paz Suárez y Eli Emmanuel Linares Romero declaramos que esta solución
#es fruto exclusivamente nuestro trabajo personal. No hemos sido
#ayudados por ninguna otra persona ni hemos obtenido la solución de
#fuentes externas, y tampoco hemos compartido nuestra solución con
#nadie. Declaramos además que no hemos realizado de manera deshonesta
#ninguna otra actividad que pueda mejorar nuestros resultados
#ni perjudicar los resultados de los demás.

# Lab 06 Puesto 01
# Gestion de la Informacion en la Web - 2016-2017
# Universidad Complutense de Madrid
# Madrid
# MongoEngine

from mongoengine import *
import re
import datetime
connect('giw_mongoengine')

# Definicion del esquema
class Usuario(Document):
    dni = StringField(required = True, unique = true, regex = "(\d{8}-?[A-Z]|[X-Z]-?\d{7}-?[A-Z])")
    nombre = StringField(required = true)
    primer_apellido = StringField(required = true)
    segundo_apellido = StringField()
    fecha_nac = StringField(required=true, regex = "\d{4}-\d{2}-\d{2}")
    ultimos_accesos = ListField(ComplexDateTimeField())#ComplexDateTimeField()
    tarjetas = ListField(EmbeddedDocumentField(Credit_card))
    pedidos = ListField(ReferenceField(Pedido, reverse_delete_rule = mongoengine.PULL))

    def clean(self):

        #Primero se valida que el DNI tenga formato correcto

        #Tabla de digitos de control
        dic = dict()
        dic[0] = "T"
        dic[1] = "R"
        dic[2] = "W"
        dic[3] = "A"
        dic[4] = "G"
        dic[5] = "M"
        dic[6] = "Y"
        dic[7] = "F"
        dic[8] = "P"
        dic[9] = "D"
        dic[10] = "X"
        dic[11] = "B"
        dic[12] = "N"
        dic[13] = "J"
        dic[14] = "Z"
        dic[15] = "S"
        dic[16] = "Q"
        dic[17] = "V"
        dic[18] = "H"
        dic[19] = "L"
        dic[20] = "C"
        dic[21] = "K"
        dic[22] = "E"

        #Tabla de sustitucion para extranjeros
        dic_ex = dict()
        dic_ex["X"] = "0"
        dic_ex["Y"] = "1"
        dic_ex["Z"] = "2"

        #Se obtiene el numero del dni en formato string
        numero_match = re.search("\d+", self.dni)
        numero_string = numero_match.group(1)

        #Se obtiene el digito de control, el cual es el último caracter
        digito_control = self.dni[-1]

        #Si son 8 digitos, es dni español y se puede traducir directamente el numero a int.
        if len(numero_string) == 8:
            numero = int(numero_string)
        #Si no, son 7 digitos y es nie para extranjeros. Hace falta cambiar la primera letra por su numero.
        else:
            numero = int(dic_ex[numero_match.string[0]] + numero_string)

        #Se valida el digito de control.
        if dic[numero % 23] != digito_control:
            raise ValidationError("El digito de control no es correcto. Verifique DNI")

        #Una vez validado el DNI, se asegura de que la lista de accesos sean los últimos 10 accesos
        if len(self.ultimos_accesos) > 10:
            self.ultimos_accesos = self.ultimos_accesos[len(self.ultimos_accesos) - 10:]

        #Se valida que la fecha de nacimiento sea una fecha válida
        try:
            datetime.datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha de nacimiento no es una fecha válida o no está en el formato correcto." +
                             " (\"AAAA-MM-DD\")")

class Credit_card(EmbeddedDocument):
    owner = StringField(required = true)
    number = StringField(required = true, min_length = 16, max_length = 16, regex = "\d{16}")
    month_expire = StringField(required = true, min_length = 2, max_length = 2, regex = "^0[1-9]$|^1[0-2]$")
    year_expire = StringField(required = true, min_length = 2, max_length = 2, regex = "\d{2}")
    CVV = StringField(required = true, min_length = 3, max_length = 3, regex = "\d{3}")

class Pedido (Document):
    precio_total = FloatField(required = True)
    fecha = ComplexDateTimeField(required = True)
    lineas = ListField(EmbeddedDocumentField(Linea_pedido), required = True)

    def clean(self):
        suma = 0
        for linea in self.lineas:
            suma += linea.precio_total

        if suma != self.precio_total:
            raise ValidationError("El precio total del pedido no coincide con los precios totales de las lineas " +
                                  "del pedido")

class Linea_pedido(EmbeddedDocument):
    cantidad = IntField(required = True, min_value = 1)
    precio_unidad = FloatField(required = True)
    nombre_producto = StringField(required = True)
    precio_total = FloatField (required = True)
    ref_product = ReferenceField(Producto, required = true)

    def clean(self):
        if self.cantidad * self.precio_unidad != self.precio_total:
            raise ValidationError("El precio total en la linea de pedido no es correcto.")



#TODO FORMATO
class Producto(Document):
    #Falta el formato
    codigo_de_barras = StringField(required = true, unique = true, regex = "")
    name = StringField(required = true, min_length = 1)
    main_category  = IntField(min_value = 1)
    category_list = ListField(IntField(min_value = 1))

def clean(self):

    #Validación 1º
    dic = dict()
    dic[0] = "T"
    dic[1] = "R"
    dic[2] = "W"
    dic[3] = "A"
    dic[4] = "G"
    dic[5] = "M"
    dic[6] = "Y"
    dic[7] = "F"
    dic[8] = "P"
    dic[9] = "D"
    dic[10] = "X"
    dic[11] = "B"
    dic[12] = "N"
    dic[13] = "J"
    dic[14] = "Z"
    dic[15] = "S"
    dic[16] = "Q"
    dic[17] = "V"
    dic[18] = "H"
    dic[19] = "L"
    dic[20] = "C"
    dic[21] = "K"
    dic[22] = "E"

    if (self.tipo == "Usuario"):
        numero = self.dni[7] % 23
        if(self.dni[8] != dic[numero]):
            raise ValidationError("La letra del DNI no es válida")

    #Validacion 3º - Hecho
    if (self.tipo == "Linea_pedido") and (self.precio_total != (cantidad*precio_unidad)):
         raise ValidationError("El precio total debe ser igual a la multiplicacion de la cantidad por el precio de la unidad")

    #Validacion 4º -Hecho
    if(self.tipo == "Linea_pedido" and self.nombre_producto != ref_product.name):
        raise ValidationError("El nombre del producto de la linea de pedido no es equivalente al nombre del producto referenciado")

    #Validacion 5º


    #Validacion 6º
    if( self.tipo == "Producto" and self.category_list.length > 0 and self.category_list[0] != self.main_category):
        raise ValidationError("Su categoria principal no aparece en primer lugar en la lista de categorias secundarias")

    #Validacion 7º - Hecho


def insertar():

    #Creamos las tres tarjetas
    credit_card1 = Credit_card("Pepe","123456789012","01","20","123")
    credit_card2 = Credit_card("Pepa","098765432109", "02","19","321")
    credit_card3 = Credit_card("Jose","135679087356", "03","21","541")

    #Creamos los productos
    product1 = Producto("","bmw serie 1","bmw",["bmw","coche","medio de transporte"])
    product2 = Producto("","huawei version 3","huawei")
    product3 = Producto("","radiocaset","dispositivo")

    orden_line = Linea_De_Pedidos(2, 5.50, "bmw serie 1", 11.0,product1)

    #Creamos los usuarios
    userOne = Usuario("50645712B",)
    userTwo = Usuario("", )

def main():
    print "Hola"

main()
