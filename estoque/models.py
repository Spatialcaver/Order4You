from django.db import models
import uuid



UNIDADE_DE_MEDIDA = [
    ("KG", "Quilograma"),
    ("G", "Grama"),
    ("L", "Litro"),
    ("ML", "Mililitro"),
    ("UN", "Unidade"),
]



class MateriaPrima(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50, null=False, blank=False)
    unidade_medida = models.CharField(max_length=30, choices=UNIDADE_DE_MEDIDA, null=False, blank=False)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    estoque_minimo = models.IntegerField(null=False, blank=False, default=1)
    
    
    def __str__(self):
        return (self.nome, self.unidade_medida)


class Estoque(models.Model):
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False, default=0)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.materia_prima.nome} - {self.quantidade} {self.materia_prima.unidade_medida}"
    


class Movimentacao(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False, default=0)
    tipo_movimentacao = models.CharField(max_length=20, choices=[("ENTRADA", "Entrada"), ("SAIDA", "Saída")], null=False, blank=False)
    data_movimentacao = models.DateTimeField(auto_now=True)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.materia_prima.nome} - {self.quantidade} {self.materia_prima.unidade_medida}"
    

class Fornecedor(models.Model):
    id = models.URLField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    produto = models.ManyToManyField(MateriaPrima, blank=True)

    def __str__(self):
        return self.nome