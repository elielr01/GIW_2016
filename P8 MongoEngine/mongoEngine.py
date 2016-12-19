# -*- coding: utf-8 -*-
# Practica 8 - MongoEngine

#Juan Mas Aguilar, Lorenzo De La Paz Suárez y Eli Emmanuel Linares Romero declaramos que esta solución
#es fruto exclusivamente nuestro trabajo personal. No hemos sido
#ayudados por ninguna otra persona ni hemos obtenido la solución de
#fuentes externas, y tampoco hemos compartido nuestra solución con
#nadie. Declaramos además que no hemos realizado de manera deshonesta
#ninguna otra actividad que pueda mejorar nuestros resultados
#ni perjudicar los resultados de los demás.

# Lab 06 Puesto 02
# Gestion de la Informacion en la Web - 2016-2017
# Universidad Complutense de Madrid
# Madrid
# MongoEngine

from mongoengine import *
connect('giw_mongoengine')

#Clase Trajeta de Credito
class Credit_card(EmbeddedDocument):
    owner = StringField(required = True, min_length=1, max_length=10,unique=true)
    number = StringField(required = True,min_length=16,max_length=16)
    month_expire = StringField(required = True,min_length=2,max_length=2)
    year_expire = StringField(required = True,min_length=2,max_length=2)
    CVV = StringField(required = True,min_length=3, max_length=3) 

#Clase pedido
class Pedido(Document):
    precio_total = FloatField(required = True)
    fecha = ComplexDateTimeField(required = True)
    order_line = ListField(EmbeddedDocumentField(Linea_pedido),required=True)
    

#Clase Linea de pedido
class Linea_pedido(Document) :
    cantidad = IntField(required=True, min_value=1, max_value=100)
    precio_unidad = FloatField(required=True, min_value=0.01, max_value=1000.00)
    nombre_producto = StringField(required=True,min_length=1, max_length=10)
    precio_total = FloatField (required = True,min_value=0.01, max_value=10000.00)
    ref_product = ReferenceField(Producto, required = True)

#Clase producto
class Producto(Document):
    #Falta el formato
    codigo_de_barras = StringField(required=True,unique=True,regex="[0-9]+", min_length=13,max_length=13)
    name = StringField(required=True,min_length = 1, max_length = 10)
    main_category  = IntField(required=True, min_value=0, max_value = 100)
    category_list = ListField(IntField(min_value=0, max_value=100))

#Clase Usuario -> Falta el regex
class Usuario(Document) :
    dni = StringField(required=True, unique = True, max_length = 9, regex = "[0-9]+[A-Z]")
    nombre = StringField(required=True,min_length=1, max_length=10)
    primer_apellido = StringField(required=True,min_length=1, max_length=10)
    segundo_apellido = StringField(min_length=1, max_length=10)
    fecha_nac = StringField(required=True, regex = "[0-9][0-9][0-9][0-9]'-'[0-9][0-9]'-'[0-9][0-9]")
    ultimos_accesos = ComplexDateTimeField()
    tarjetas = ListField(EmbeddedDocumentField(Credit_card))
    pedidos = ListField(ReferenceField(Pedidos, reverse_delete_rule=PULL))
    
#Función para la validacion
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
    #https://es.wikipedia.org/wiki/European_Article_Number

    #Validacion 6º
    if( self.tipo == "Producto" and self.category_list.length > 0 and self.category_list[0] != self.main_category):
        raise ValidationError("Su categoria principal no aparece en primer lugar en la lista de categorias secundarias")

    #Validacion 7º - Hecho
    
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


insertar()
