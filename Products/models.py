from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Proveedore(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.TextField()
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    descripcion = models.TextField()
    imagen = models.ImageField(
        upload_to='imgProductos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedore, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# class Cliente(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     telefono = models.CharField(max_length=50)
#     direccion = models.TextField()
#     fecha_registro = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.nombre + ' ' + self.apellido


class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = property(lambda self: self.producto.precio * self.cantidad)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # + ' - ' + 'Cliente: ' + self.usuario
        return 'Producto: ' + self.producto.nombre + ' - ' + 'Cantidad: ' + str(self.cantidad) + ' - ' + 'Precio: ' + '$' + str(self.producto.precio) + ' - ' + 'Total: ' + '$' + str(self.total)
