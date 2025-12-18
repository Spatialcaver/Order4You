from django.urls import path
from user.views import CreateUserView, UserUpdateView, UserDeleteView, UserListView, ClienteCreate, ClienteList, ClienteUpdate

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create-user'),
    path('update/<pk>/', UserUpdateView.as_view(), name='update-user'),
    path('delete/<pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('list/', UserListView.as_view(), name='list-users'),
    path('cliente/create/', ClienteCreate.as_view(), name='create-cliente'),
    path('cliente/list/', ClienteList.as_view(), name='list-clientes'),
    path('cliente/update/<pk>/', ClienteUpdate.as_view(), name='update-cliente'),
]