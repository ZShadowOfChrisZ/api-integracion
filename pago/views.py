from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User as Usuario
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from carro.models import Carro
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from inventario.models import Producto

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def pagarCarro(request):
    if(request.user.id):
        carros = Carro.objects.filter(id_usuario=request.user.id)
        productos = list()
        total = 0
        for carro in carros:
            total += carro.id_producto.precio * carro.cantidad
            producto = dict({'producto': carro.id_producto.nombre, 'cantidad': carro.cantidad, 'precio': (carro.id_producto.precio * carro.cantidad)})
            productos.append(producto)
        return Response({'respuesta': 'pago_realizado','total_pagado':total,'detalle_pago': productos}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Usuario sin carro', 'estado_pago' : 'Pago rechazado'}, status=status.HTTP_200_OK)