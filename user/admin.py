from django.contrib import admin
from user.models import User, Cliente



class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'full_name', 'username', 'email', 'perfil')
    search_fields = ('username', 'full_name', 'id')
    

admin.site.register(User, UserAdmin)



class ClienteAdmin(admin.ModelAdmin):

    list_display = ('id', 'nome__full_name', 'telefone', 'endereco')
    search_fields = ('nome', 'telefone', 'endereco')

admin.site.register(Cliente, ClienteAdmin)