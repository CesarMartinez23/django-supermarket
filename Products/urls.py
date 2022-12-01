from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.signin, name="login"),
    path('logout/', views.close_session, name="logout"),
    path('register/', views.register, name="register"),

    # Products
    path('new_product/', views.new_product, name="new_product"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),

    # Categories
    path('categories/', views.categories, name="categories"),
    path('new_category/', views.new_category, name="new_category"),
    path('update_category/<int:id>', views.update_category, name="update_category"),
    path('delete_category/<int:id>', views.delete_category, name="delete_category"),

    # Providers
    path('providers/', views.providers, name="providers"),
    path('new_provider/', views.new_provider, name="new_provider"),
    path('update_provider/<int:id>', views.update_provider, name="update_provider"),
    path('delete_provider/<int:id>', views.delete_provider, name="delete_provider"),

    # # Customers
    # path('customers/', views.customers, name="customers"),
    # path('new_customer/', views.new_customer, name="new_customer"),
    # path('update_customer/<int:id>', views.update_customer, name="update_customer"),
    # path('delete_customer/<int:id>', views.delete_customer, name="delete_customer"),

    # Carts
    path('cart/', views.cart, name="cart"),
    path('add_cart/<int:id>', views.add_cart, name="add_cart"),
    path('delete_cart/<int:id>', views.delete_cart, name="delete_cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
