from django.shortcuts import render, redirect
from .models import Producto, Categoria, Proveedore
from .forms import ProductoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
    return render(request, 'pages/login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('products')
    return render(request, 'pages/register.html')

def close_session(request):
    logout(request)
    return redirect('home')

def new_product(request):
    new_product = ProductoForm()
    catgeorias = Categoria.objects.all()
    proveedores = Proveedore.objects.all()
    
    if request.method == 'POST':
        producto = Producto.objects.create(
        nombre = request.POST.get('nombre'),
        cantidad = request.POST.get('cantidad'),
        precio = request.POST.get('precio'),
        descripcion = request.POST.get('descripcion'),
        imagen = request.FILES.get('imagen'),
        categoria = Categoria.objects.get(id=request.POST.get('categoria')),
        proveedor = Proveedore.objects.get(id=request.POST.get('proveedor'))
        )
        producto.save()
    
        return redirect('products')

    return render(request, 'crud/insert.html', {
        'categorias': catgeorias,
        'proveedores': proveedores,
        'form': new_product
    })

def update_product(request, id):
    producto = Producto.objects.get(id=id)
    catgeorias = Categoria.objects.all()
    proveedores = Proveedore.objects.all()
    print(producto)
    
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.cantidad = request.POST.get('cantidad')
        producto.precio = request.POST.get('precio')
        producto.descripcion = request.POST.get('descripcion')
        producto.imagen = request.FILES.get('imagen') if request.FILES.get('imagen') != None else producto.imagen
        producto.categoria = Categoria.objects.get(id=request.POST.get('categoria'))
        producto.proveedor = Proveedore.objects.get(id=request.POST.get('proveedor'))
        producto.save()
        return redirect('products')
    return render(request, 'crud/update.html', {
        'producto': producto,
        'categorias': catgeorias,
        'proveedores': proveedores,
    })


def delete_product(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('products')