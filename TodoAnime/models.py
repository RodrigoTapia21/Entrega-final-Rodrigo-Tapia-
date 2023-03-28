from django.db import models
from django.contrib.auth.models import User


class Otaku(models.Model):
    Nombre_anime=models.CharField(max_length=40)
    Tipo_anime=models.CharField(max_length=10)
    Descripcion=models.CharField(max_length=120)
    creado_el=  models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    
    
    def __str__(self):
        return f"{self.id} - {self.Nombre_anime} - {self.publisher.username}"
