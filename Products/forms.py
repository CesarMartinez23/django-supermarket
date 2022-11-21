from django import forms
from .models import Producto, Categoria, Proveedore

class ProductoForm(forms.Form):
    nombre = forms.CharField(required=True)
    cantidad = forms.IntegerField(required=True)
    precio = forms.FloatField(min_value=0.0)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 20}))
    imagen = forms.ImageField()
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    proveedor = forms.ModelChoiceField(queryset=Proveedore.objects.all())
    