from django.db import models
import uuid
from estoque.models import MateriaPrima


CATEGORIAS=[
    # PRODUÇÃO PRÓPRIA
    ('PIZZA_CLASSICA', 'Pizzas Clássicas'),
    ('PIZZA_ESPECIAL', 'Pizzas Especiais'),
    ('ESFIHA', 'Esfihas e Salgados'),
    ('PRODUCAO_DOCE', 'Sobremesas de Produção'), # Ex: Açaí, Brownie
    
    # REVENDA (Itens comprados prontos e com baixa direta no estoque do produto final)
    ('REFRIGERANTE', 'Refrigerantes'),
    ('CERVEJA', 'Cervejas'),
    ('SUCO_AGUA', 'Sucos e Águas'),
    ('REVENDA_DOCE', 'Sobremesas Industrializadas'), # Ex: Sorvetes prontos
    
    # EXTRAS E ADICIONAIS (Podem ser Revenda ou alterar a composição de outro produto)
    ('ADICIONAL', 'Adicionais de Sabor'), # Ex: Queijo Extra, Bacon, Borda
    ('COMBO', 'Combos e Promoções'), # Usado para agrupamento lógico, não é um item físico
]


# Create your models here.
class Category(models.Model):
    Category = models.CharField(max_length=100, blank=True, choices=CATEGORIAS)
    


class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_avaliable = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.id, self.nome, self.categoria, self.preco, self.is_avaliable


class ComposicaoProduto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    produto_composto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='composto_por')
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    materia_prima = models.ForeignKey('MateriaPrima', on_delete=models.CASCADE, related_name='materia_prima', blank=False, null=False)
    
    
    def __str__(self):
        return self.id, self.produto, self.produto_composto, self.quantidade, self.materia_prima