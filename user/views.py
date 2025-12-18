from django.shortcuts import render
from user.serializer import CreateUserSerializer, UserUpdateAndDeleteSerializer, ClienteSerializer, ListUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from user.models import User, Cliente
from django.shortcuts import get_object_or_404 
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import    extend_schema


# Create your views here.

class CreateUserView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request =  CreateUserSerializer,
        
        responses = {
            201: CreateUserSerializer,
            400: "Bad Request"
        }, 
        tags = ["User"],
        description = 'Rota para criação de usuario, devem ser passados, username, senha, e-mail e demais campos obrigatórios. ',
        
)
    
    
    def post(self, request):
        try:
            serializer_class = CreateUserSerializer(data=request.data)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            return Response({'message': 'User created successfully', 'data': serializer_class.data},status=status.HTTP_201_CREATED)
            
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request = UserUpdateAndDeleteSerializer,
        responses = {
            200: UserUpdateAndDeleteSerializer,
            400: "Bad Request",
            404: "Not Found"
        },
        tags = ["User"],
        description = 'Rota para atualização de usuario, devem ser passados, os campos a serem atualizados. '
    )

    def patch(self, request,pk, *args, **kwargs):
        try:
            user = get_object_or_404(User, pk=pk)
            serializer_class = UserUpdateAndDeleteSerializer(user, data=request.data, partial=True)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            return Response({'message': 'User updated successfully', 'data': serializer_class.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
        


class UserDeleteView(APIView):

    @extend_schema(
        request = UserUpdateAndDeleteSerializer,
        responses = {
            200: UserUpdateAndDeleteSerializer,
            400: "Bad Request",
            404: "Not Found"
        },
        tags = ["User"],
        description = 'Rota para  exclusão de usuario, deve se passado o ID do usuario para exclusão. '
    )    
        
        

    def delete(self, request, pk, *args, **kwargs):
        try:
            user = get_object_or_404(get_user_model(), pk=pk)
            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={
            200: "List of users",
            404: "Not Found"
        },
        tags=["User"],
        description='Rota para listagem de usuarios, não espera nenhum parâmetro.'
    )

    def get(self, request):
        try:
            users = get_user_model().objects.all()
            serializer_class = ListUser(users, many=True)
            return Response({'message': 'Users listed successfully', 'data': serializer_class.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
class ClienteCreate(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ClienteSerializer,
        responses={
            201: ClienteSerializer,
            400: "Bad Request"
        },
        tags=["Cliente"],
        description='Rota para criação de cliente (por padrão o cliente é criado no ato da criação do usuário, essa rota deve ser usada apenas em casos específicos), devem ser passados, os campos ID do user (O cliente deve obrigatoriamente ser um usuário cadastrado), telefone e endereço .'
    )

    def post(self, request):
        try:
            serializer_class = ClienteSerializer(data=request.data)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            return Response({'message': 'Cliente created successfully', 'data': serializer_class.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ClienteList(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        responses={
            200: "List of clientes",
            404: "Not Found"
        },
        tags=["Cliente"],
        description='Rota para listagem de clientes, não espera nenhum parâmetro.'
    )

    def get(self, request):
        try:
            clientes = Cliente.objects.all()
            serializer_class = ClienteSerializer(clientes, many=True)
            return Response({'message': 'Clientes listed successfully', 'data': serializer_class.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        


class ClienteUpdate(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ClienteSerializer,
        responses={
            200: ClienteSerializer,
            400: "Bad Request",
            404: "Not Found"
        },
        tags=["Cliente"],
        description='Rota para atualização de cliente, deve ser passado o ID do cliente para atualização, e o campo a ser atualizado.'
    )

    def put(self, request, pk, *args, **kwargs):
        try:
            cliente = get_object_or_404(Cliente, pk=pk)
            serializer_class = ClienteSerializer(cliente, data=request.data)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            return Response({'message': 'Cliente updated successfully', 'data': serializer_class.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)