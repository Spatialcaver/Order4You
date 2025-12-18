from django.shortcuts import render
from venda.serializer import ListVendaSerializer, VendaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404 
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from drf_spectacular.utils import    extend_schema

from venda.models import Venda


# Create your views here.

class CreateVenda(APIView):
    def post(self, request):
        try:
            serializer_class = VendaSerializer(data=request.data)
            
            
        except Exception as e:
            return Response({'error': str(e)})
        
        
        
        
class ListVenda(APIView):
    
    def get(self, request):
        try:
            queryset = Venda.objects.all()
            serializer = ListVendaSerializer(queryset, many=True)

            return Response({'result': serializer.data}, status=status.HTTP_200_OK)
        
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)