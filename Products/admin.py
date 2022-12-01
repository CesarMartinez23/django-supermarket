from django.contrib import admin
from .models import Categoria, Proveedore, Producto, Carrito  # , Cliente

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Proveedore)
admin.site.register(Producto)
# admin.site.register(Cliente)
admin.site.register(Carrito)
