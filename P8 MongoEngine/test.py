# -*- coding: utf-8 -*-
from mongoengine import *
import re
import datetime
connect("eli")

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


unProducto  = Producto("1234567890418", "Atun", 1, [2])

unProducto.save()


unaLinea = Linea_pedido(10, 20, "Atun", 200, unProducto)
#otraLinea = Linea_pedido(8, 20, "Atun", 160)


unPedido = Pedido(200, datetime.datetime.now(), [unaLinea])

unPedido.save()
