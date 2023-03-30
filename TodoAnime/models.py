from django.db import models
from django.contrib.auth.models import User


class Otaku(models.Model):
    Nombre_anime=models.CharField(max_length=40)
    Tipo_anime=models.CharField(max_length=10)
    Descripcion=models.CharField(max_length=120)
    creado_el = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    image = models.ImageField(upload_to="portada", null=True, blank=True)
    
    property
    def image_url(self):
        return self.image.url if self.image else ''
    
    def __str__(self):
        return f"{self.id} - {self.Nombre_anime} - {self.publisher.username}"
    
    
class Perfil(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="perfil")
    redes_sociales = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    
class Mensaje(models.Model):
    mensaje = models.TextField(max_length=100)
    email = models.EmailField()
    creado_el = models.DateTimeField(auto_now_add=True) 
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes")
    
