from django.urls import path
from .views import ProductoListaCrear, ProductoDetalle

urlpatterns = [
    path('listar_productos/', ProductoListaCrear.as_view(), name='producto-lista-crear'),
    path('listar_productos_by_id/<int:pk>/', ProductoDetalle.as_view(), name='producto-detalle'),
]