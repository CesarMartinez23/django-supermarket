from django.test import TestCase
from Products.tests.testProduct import createProducto
from Products.models import Carrito, Producto


class createCarrito(TestCase):

    def test_createCarrito(self):
        createProducto.test_createProducto(self)

        Carrito.objects.create(producto=Producto.objects.get(id=1), cantidad=1)
