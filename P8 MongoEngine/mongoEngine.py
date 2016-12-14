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

from mongoengine import connect
connect('giw_mongoengine')

class Usuario(document):
    dni = StringField(required=true, unique = true, max_length = 9, regex = "[0-9]+[A-Z]")
    nombre = StringField(required=true)
    primer_apellido = StringField(required=true)
    segundo_apellido = StringField()
    fecha_nac = StringField(required=true, regex = "")
    ultimos_accesos = ComplexDateTimeField()
    tarjetas = ListField(EmbeddedDocumentField(Credit_card))
    pedidos = ListField(ReferenceField(Pedidos, reverse_delete_rule=PULL))


class Credit_card(EmbeddedDocument):
    owner = StringField(required=true, min_length=1, max_length=10,unique=true)
    number = StringField(required=true,min_length=16,max_length=16)
    month_expire = StringField(required=true,min_length=2,max_length=2)
    year_expire = StringField(required=true,min_length=2,max_length=2)
    CVV = StringField(required=true,max_length=3) 


class Linea_pedido(document):
    cantidad = IntField(required=true, min_value=1)
    precio_unidad = FloatField(required=true)
    nombre_producto = StringField(required=true)
    precio_total = FloatField (required = true)
    ref_product = ReferenceField(Producto, required = true)

class Producto(Document):
    #Falta el formato
    codigo_de_barras = StringField(required=true,unique=true,regex="")
    name = StringField(required=true,min_length = 1, max_length = 10)
    main_category  = IntField(max_value = 100)
    category_list = ListField(IntField(min_value=0, max_value=100))

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
