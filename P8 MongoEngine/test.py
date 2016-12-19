# -*- coding: utf-8 -*-
from mongoengine import *
import re
import datetime
connect("eli")

class Linea_pedido(EmbeddedDocument):
    cantidad = IntField(required = True, min_value = 1)
    precio_unidad = FloatField(required = True)
    nombre_producto = StringField(required = True)
    precio_total = FloatField (required = True)
    ref_product = ReferenceField(Producto, required = true)


    def clean(self):
        if self.cantidad * self.precio_unidad != self.precio_total:
            raise ValidationError("El precio total en la linea de pedido no es correcto.")

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


unaLinea = Linea_pedido(10, 20, "Atun", 200)
otraLinea = Linea_pedido(8, 20, "Atun", 160)


unPedido = Pedido(360, datetime.datetime.now(), [unaLinea, otraLinea])

unPedido.save()
