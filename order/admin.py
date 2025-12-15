from django.contrib import admin
from order.models import Order, ItemPedido, Payment

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status', 'data_pedido', 'valor_total')
    search_fields = ('id', 'cliente', 'status')

admin.site.register(Order, OrderAdmin)


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'preco_unitario')
    search_fields = ('pedido', 'produto')


admin.site.register(ItemPedido, ItemPedidoAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'metodo_pagamento', 'status_pagamento')
    search_fields = ('id', 'pedido', 'metodo_pagamento')

admin.site.register(Payment, PaymentAdmin)