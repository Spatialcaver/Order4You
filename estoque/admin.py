from django.contrib import admin
from estoque.models import Estoque,MateriaPrima,Fornecedor, Movimentacao

# Register your models here.
admin.site.register(Estoque)


admin.site.register(MateriaPrima)


admin.site.register(Fornecedor)


admin.site.register(Movimentacao)