from mongoengine import connect

connect("giw_mongoengine")

class pedido (Document):
    precio_total = FloatField(required = true)
    fecha = ComplexDateTimeField(required = true)
