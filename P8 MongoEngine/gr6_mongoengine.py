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
    dni = StringField(required = True, unique = True, regex = "(\d{8}-?[A-Z]|[X-Z]-?\d{7}-?[A-Z])")
    nombre = StringField(required = True)
    primer_apellido = StringField(required = True)
    segundo_apellido = StringField()
    fecha_nac = StringField(required=True, regex = "\d{4}-\d{2}-\d{2}")
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
    owner = StringField(required = True)
    number = StringField(required = True, min_length = 16, max_length = 16, regex = "\d{16}")
    month_expire = StringField(required = True, min_length = 2, max_length = 2, regex = "^0[1-9]$|^1[0-2]$")
    year_expire = StringField(required = True, min_length = 2, max_length = 2, regex = "\d{2}")
    CVV = StringField(required = True, min_length = 3, max_length = 3, regex = "\d{3}")

class Producto(Document):
    codigo_de_barras = StringField(required = True, unique = True)
    name = StringField(required = True, min_length = 1)
    main_category  = IntField(min_value = 1)
    category_list = ListField(IntField(min_value = 1))

    def clean(self):
        #Primero se valida el formado del codigo de barras
        suma = 0
        for i, digit in enumerate(reversed(self.codigo_de_barras[:-1])):
            suma += int(digit) * 3 if (i % 2 == 0) else int(digit)

        digito_control = (10 - (suma % 10)) % 10

        if self.codigo_de_barras[-1] != str(digito_control):
            raise ValidationError("El codigo de barras no respeta el formato EAN-13")

        #Despues, se agrega la categoría principal a la lista de categorías secundarias (si ésta existiera)
        if len(self.category_list) != 0:
            self.category_list = [self.main_category] + self.category_list

class Linea_pedido(EmbeddedDocument):
    cantidad = IntField(required = True, min_value = 1)
    precio_unidad = FloatField(required = True)
    nombre_producto = StringField(required = True)
    precio_total = FloatField (required = True)
    ref_product = ReferenceField(Producto, required = True)

    def clean(self):
        #Se valida primero que el precio total de la linea sea el correcto
        if self.cantidad * self.precio_unidad != self.precio_total:
            raise ValidationError("El precio total en la linea de pedido no es correcto.")

        #Despues se valida que el nombre del producto en esta línea sea el mismo que el producto referenciado
        if self.ref_product.name != self.nombre_producto:
            raise ValidationError("El nombre del producto de la linea no coincide con el del producto referenciado")

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


#Funcion para la inserción
def insertar():

    #Credit cards created
    credit_card1 = Credit_card("Pepe","123456789012","01","20","123")
    credit_card2 = Credit_card("Pepe","098765432109","02","19","321")
    credit_card3 = Credit_card("Pepa","135679087356","03","21","541")
    credit_card4 = Credit_card("Pepe","374970681357","05","25","409")

    #Creamos los productos
    product1 = Producto("1234567890123","bmw serie 1","bmw",["bmw","coche","medio de transporte"])
    product2 = Producto("1234567890124","huawei version 3","huawei")
    product3 = Producto("1234567890321","radiocaset","dispositivo")
    product4 = Producto("1234567890796","Lenovo FR435","portatil",["portatil","gama alta"])
    product5 = Producto("1234567890642","Camiseta del Real Madrid","camiseta",["camiseta","alta calidad"])
    product6 = Producto("123456789036","Sudadera del Atlético de Madrid","sudadera")

    #Order lines created
    order_line1 = Linea_De_Pedido(2, 450.95, "coche-bmw serie 1", 901.90,product1)
    order_line2= Linea_De_Pedido(3,123.00,"movil-huawei version 3",369.00,product2)
    order_line3 = Linea_De_Pedido(5,2.35,"musica-radiocaset",11.75,product3)
    order_line4 = Linea_De_Pedido(1,367.50,"portatil-Lenovo FR435",367.50,product4)
    order_line5 = Linea_De_Pedido(4,45.60,"camiseta-Camiseta del Real Madrid",182.40,product5)
    order_line6 = Linea_De_Pedido(2,39.70,"sudadera-Sudadera del Atlético de Madrid",79.40,product6)

    #Orders created
    order1 = Pedido(913.65,datetime.datetime.now().time(),[order_line1,order_line3])
    order2 = Pedido(736,50,datetime.datetime.now().time(),[order_line2,order_line4])
    order3 = Pedido(629.30,datetime.datetime.now().time(),[order_line5,order_line6,order_line4])
    order4 = Pedido(981.30,datetime.datetime.now().time(),[order_line1,order_line6])
    order5 = Pedido(551.40,datetime.datetime.now().time(),[order_line2,order_line5])

    #Creamos los usuarios
    userOne = Usuario("50645712B","Pepe","García","1996-11-21","",[credit_card1,credit_card2,credit_card4],[order1,order2])
    userTwo = Usuario("12345678T","Pepa","Fernández","1995-01-12","",[credit_card3],[order3,order4,order5])
    #userThree = Usuario(dni="098765432137",nombre="Elí",fecha_nacimiento="1990-05-17")

    #Guardamos los productos en la BBDD
    product1.save()
    product2.save()
    product3.save()
    product4.save()
    product5.save()
    product6.save()

    #Guardamos los pedidos en la BBDD
    order1.save();
    order2.save();
    order3.save();
    order4.save();
    order5.save();

    #Guardamos los usuarios en la BBDD
    userOne.save()
    userTwo.save()
    #userThree.save()

def main():
    print "Hola"

main()
