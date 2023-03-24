from django.db import models


class Otaku(models.Model):
    Nombre_anime=models.CharField(max_length=40)
    Tipo_anime=models.CharField(max_length=10)
    descripcion=models.CharField(max_length=120)
    creado_el=  models.DateTimeField(auto_now_add=True)
    
