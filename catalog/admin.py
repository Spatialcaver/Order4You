from django.contrib import admin
from catalog.models import Category, Produto, ComposicaoProduto


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category',)
    search_fields = ('Category',)

admin.site.register(Category, CategoryAdmin)



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'preco')
    search_fields = ('id', 'nome', 'preco')

admin.site.register(Produto, ProdutoAdmin)


class ComposicaoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'materia_prima')
    search_fields = ('id', 'produto', 'materia_prima')

admin.site.register(ComposicaoProduto, ComposicaoProdutoAdmin)