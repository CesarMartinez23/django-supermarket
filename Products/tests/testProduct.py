from django.test import TestCase
from Products.models import Producto, Categoria, Proveedore


class createProducto(TestCase):

    def test_createProducto(self):
        Categoria.objects.create(nombre='test', descripcion='test')

        Proveedore.objects.create(
            nombre='test', telefono='7000-0000', direccion='test',  email='test', fecha_registro='2020-01-01')

        Producto.objects.create(nombre='test', cantidad=1, precio=1.0, descripcion='test',
                                categoria=Categoria.objects.get(id=1), proveedor=Proveedore.objects.get(id=1))
