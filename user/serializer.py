from user.models import User, Cliente
from rest_framework import serializers
from django.utils import timezone


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ('id',)
        


class ListUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'is_active', 'is_staff','is_superuser', 'date_joined', 'username', 'email', 'full_name', 'perfil')

        read_only_fields = ('id', 'date_joined', 'username')



class UserUpdateAndDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ('id', 'username', 'date_joined')
        

class ClienteSerializer(serializers.ModelSerializer):
    # 'user' deve ser o nome do campo ForeignKey no seu modelo Cliente.
    # 'slug_field' deve ser exatamente o nome do atributo no modelo User que você quer exibir.
    nome = serializers.SlugRelatedField(
        slug_field='full_name', 
        read_only=True
    )

    class Meta:
        model = Cliente
        fields = ('id', 'nome', 'telefone', 'endereco') # 'user' agora retornará apenas o valor de full_name