from django.shortcuts import render
from .models import Producto


# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request):
    products = Producto.objects.all()
    print(products)
    return render(request, 'pages/products.html',{
        'products': products
    })

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')