from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import email
import uuid


TIPOS_PERFIL = [
    ('administrador', 'Administrador'),
    ('gerente', 'Gerente'),
    ('funcionario', 'Funcionário'),
    ('cliente', 'Cliente')
]

# Create your models
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True, blank=False, editable=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    perfil = models.CharField(max_length=20, unique=True, blank=False, choices=TIPOS_PERFIL)
    name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    full_name = models.CharField(max_length=50, blank=False, null=False)
    
    
    def __str__(self):
        return self.name, self.username


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.name, self.endereco, self.telefone
    

