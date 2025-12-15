from django.db import models
from order.models import Order, Payment


# Create your models here.

class Venda(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=100)
    pedido = models.ForeignKey(Order, on_delete=models.PROTECT)
    data_venda = models.DateTimeField(auto_now_add=True)
    valor_total = models.ForeignKey(Payment, on_delete=models.PROTECT)
    
    
    
    def __str__(self):
        return super().__str__()
    


class CustoProducao(models.Model):
    id = models.AutoField(primary_key=True)
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT)
    custo_material = models.DecimalField(max_digits=10, decimal_places=2)
    custo_operacional = models.DecimalField(on_delete=models.PROTECT)
    custo_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return super().__str__()