from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Cliente

@receiver(post_save, sender=User)
def create_cliente_for_new_user(sender, instance, created, **kwargs):
    # 'created' é um booleano que é True apenas na criação do objeto
    if created:
        Cliente.objects.create(user=instance)