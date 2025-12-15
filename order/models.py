from django.db import models
import datetime
from user.models import Cliente
from catalog.models import Produto

PAYMENT = [
    ('CREDIT_CARD', 'Credit Card'),
    ('DEBIT_CARD', 'Debit Card'),
    ('BANK_TRANSFER', 'Bank Transfer'),
    ('CASH', 'Cash')
]


STATUS = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled'),
    ('DELIVERED', 'Delivered'), 
    ('IN_PROGRESS', 'In Progress')
]
# Create your models here.
class Order(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    data_pedido = models.DateTimeField(default=datetime.datetime.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    
    def __str__(self):
        return super().__str__()
    


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return super().__str__()


class Payment(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    metodo_pagamento = models.CharField(max_length=100, choices=PAYMENT)
    data_pagamento = models.DateTimeField(default=datetime.datetime.now)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return super().__str__()