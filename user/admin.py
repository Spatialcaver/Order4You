from django.contrib import admin
from user.models import User, Cliente



class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'full_name')
    search_fields = ('username', 'full_name', 'id')
    readonly_fields = ('id', 'username')

admin.site.register(User, UserAdmin)



class ClienteAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'telefone', 'endereco')
    search_fields = ('user__username', 'telefone', 'endereco')
    readonly_fields = ('id')

admin.site.register(Cliente, ClienteAdmin)