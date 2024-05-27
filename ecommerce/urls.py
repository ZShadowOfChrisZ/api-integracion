"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include  # Asegúrate de importar include
from usuario import views as ViewUsuario
from carro import views as ViewCarro
from pago import views as ViewPago

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventario.urls')),
    re_path('api/registro', ViewUsuario.registro),
    re_path('api/acceder', ViewUsuario.inicio),
    re_path('api/agregar-carro', ViewCarro.agregarProducto),
    re_path('api/mostrar-carro', ViewCarro.mostrarProducto),
    re_path('api/pagar-carro', ViewPago.pagarCarro),
]