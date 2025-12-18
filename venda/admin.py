from django.contrib import admin
from venda.models import Venda, CustoProducao

# Register your models here.
class VendaAdmin(admin.ModelAdmin):
   
    list_display = [
        'id',
        'cliente',
        'pedido',
        'data_venda',
        'valor_total'
    ]
    
    search_fields = [
        'id', 
        'cliente__nome',
        'data_venda',
        'valor_total',
        'pedido',
    ]
    
admin.site.register(Venda, VendaAdmin)




class CustoProducaoAdmin(admin.ModelAdmin):
    list_display =[
        'id', 
        'venda',
        'custo_material', 
        'custo_operacional', 
        'custo_total'
    ]
    
    
    search_fields = [
        'id', 
        'venda',
        'custo_total'
    ]

    

admin.site.register(CustoProducao, CustoProducaoAdmin)