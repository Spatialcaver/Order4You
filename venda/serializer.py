from venda.models import Venda, CustoProducao
from rest_framework import serializers
from django.utils import timezone


class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
        read_only_fields = ('id',)
        


class ListVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
        read_only_fields = ('id', 'data_venda', 'valor_total', 'pedido', 'cliente')