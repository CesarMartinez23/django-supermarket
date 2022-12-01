from django.shortcuts import render, redirect
from .models import Producto, Categoria, Proveedore, Carrito  # , Cliente
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html')


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


@login_required(login_url='login')
def close_session(request):
    logout(request)
    return redirect('home')


# Products


def products(request):
    products = Producto.objects.all()
    return render(request, 'pages/products.html', {
        'products': products
    })


@login_required(login_url='login')
def new_product(request):
    catgeorias = Categoria.objects.all()
    proveedores = Proveedore.objects.all()

    if request.method == 'POST':
        producto = Producto.objects.create(
            nombre=request.POST.get('nombre'),
            cantidad=request.POST.get('cantidad'),
            precio=request.POST.get('precio'),
            descripcion=request.POST.get('descripcion'),
            imagen=request.FILES.get('imagen'),
            categoria=Categoria.objects.get(id=request.POST.get('categoria')),
            proveedor=Proveedore.objects.get(id=request.POST.get('proveedor'))
        )
        producto.save()

        return redirect('products')

    return render(request, 'crud/insert.html', {
        'categorias': catgeorias,
        'proveedores': proveedores,
    })


@login_required(login_url='login')
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
        producto.imagen = request.FILES.get('imagen') if request.FILES.get(
            'imagen') != None else producto.imagen
        producto.categoria = Categoria.objects.get(
            id=request.POST.get('categoria'))
        producto.proveedor = Proveedore.objects.get(
            id=request.POST.get('proveedor'))
        producto.save()
        return redirect('products')
    return render(request, 'crud/update.html', {
        'producto': producto,
        'categorias': catgeorias,
        'proveedores': proveedores,
    })


@login_required(login_url='login')
def delete_product(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('products')


# Categories


@login_required(login_url='login')
def categories(request):
    categories = Categoria.objects.all()
    print(categories)
    return render(request, 'pages/categories.html', {
        'categories': categories
    })


@login_required(login_url='login')
def new_category(request):

    if request.method == 'POST':
        category = Categoria.objects.create(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
        )
        category.save()
        return redirect('categories')
    return render(request, 'crud/insert_category.html')


def update_category(request, id):
    category = Categoria.objects.get(id=id)

    if request.method == 'POST':
        category.nombre = request.POST.get('nombre')
        category.descripcion = request.POST.get('descripcion')
        category.save()
        return redirect('categories')
    return render(request, 'crud/update_category.html', {
        'category': category
    })


@login_required(login_url='login')
def delete_category(request, id):
    category = Categoria.objects.get(id=id)
    category.delete()
    return redirect('categories')

# Providers


@login_required(login_url='login')
def providers(request):
    providers = Proveedore.objects.all()
    print(providers)
    return render(request, 'pages/providers.html', {
        'providers': providers
    })


@login_required(login_url='login')
def new_provider(request):
    if request.method == 'POST':
        provider = Proveedore.objects.create(
            nombre=request.POST.get('nombre'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            email=request.POST.get('email'),
        )
        provider.save()
        return redirect('providers')
    return render(request, 'crud/insert_provider.html')


@login_required(login_url='login')
def update_provider(request, id):
    provider = Proveedore.objects.get(id=id)
    print(provider)

    if request.method == 'POST':
        provider.nombre = request.POST.get('nombre')
        provider.telefono = request.POST.get('telefono')
        provider.direccion = request.POST.get('direccion')
        provider.email = request.POST.get('email')
        provider.save()
        return redirect('providers')
    return render(request, 'crud/update_provider.html', {
        'provider': provider
    })


@login_required(login_url='login')
def delete_provider(request, id):
    provider = Proveedore.objects.get(id=id)
    provider.delete()
    return redirect('providers')

# Customers


# @login_required(login_url='login')
# def customers(request):
#     customers = Cliente.objects.all()
#     print(customers)
#     return render(request, 'pages/customers.html', {
#         'customers': customers
#     })


# @login_required(login_url='login')
# def new_customer(request):
#     if request.method == 'POST':
#         customer = Cliente.objects.create(
#             nombre=request.POST.get('nombre'),
#             telefono=request.POST.get('telefono'),
#             direccion=request.POST.get('direccion'),
#             email=request.POST.get('email'),
#         )
#         customer.save()
#         return redirect('customers')
#     return render(request, 'crud/insert_customer.html')


# @login_required(login_url='login')
# def update_customer(request, id):
#     customer = Cliente.objects.get(id=id)
#     print(customer)

#     if request.method == 'POST':
#         customer.nombre = request.POST.get('nombre')
#         customer.telefono = request.POST.get('telefono')
#         customer.direccion = request.POST.get('direccion')
#         customer.email = request.POST.get('email')
#         customer.save()
#         return redirect('customers')
#     return render(request, 'crud/update_customer.html', {
#         'customer': customer
#     })


# @login_required(login_url='login')
# def delete_customer(request, id):
#     customer = Cliente.objects.get(id=id)
#     customer.delete()
#     return redirect('customers')


# Cart
@login_required(login_url='login')
def cart(request):
    carts = Carrito.objects.all()
    print(carts)
    return render(request, 'pages/cart.html', {
        'carts': carts
    })


def add_cart(request, id):
    cart = Carrito.objects.create(
        # usuario=User.objects.get(username=str(request.user)),
        producto=Producto.objects.get(id=id),
        cantidad=request.POST.get('cantidad'),
    )
    cart.save()
    return redirect('cart')


def delete_cart(request, id):
    cart = Carrito.objects.get(id=id)
    cart.delete()
    return redirect('cart')
