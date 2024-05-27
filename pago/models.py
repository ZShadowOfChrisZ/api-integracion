from django.db import models
from django.contrib.auth.models import User as Usuario

# Create your models here.
class Pago(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.IntegerField()