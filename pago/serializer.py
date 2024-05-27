from rest_framework import serializers
from django.contrib.auth.models import User as Usuario
from .models import Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'