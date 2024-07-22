from django.urls import path
from .views import create_user, get_users, delete_user, create_company, get_company, delete_company, create_supplier, get_supplier, delete_supplier

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('get_users/', get_users, name='get_users'),
    path('get_company/', get_company, name='get_company'),
    path('get_supplier/', get_supplier, name='get_supplier'),
    path('delete_user/<int:pk>/', delete_user, name='delete_user'),
    path('create_company/', create_company, name='create_company'),
    path('create_supplier/', create_supplier, name='create_supplier'),
    path('delete_company/<int:pk>/', delete_company, name='delete_company'),
    path('delete_supplier/<int:pk>/', delete_supplier, name='delete_supplier'),
]