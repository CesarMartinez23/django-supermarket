from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
