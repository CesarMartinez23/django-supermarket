from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('new_product/', views.new_product, name="new_product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
