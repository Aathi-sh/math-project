from django.urls import path,include
from . import views
app_name = 'create_puzzles'

urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('create/', views.item_create, name='item-create'),
    path('update/<int:pk>/', views.item_update, name='item-update'),
    path('delete/<int:pk>/', views.item_delete, name='item-delete'),
    path('confirm_delete/<int:pk>/', views.item_confirm_delete, name='item-confirm-delete'),
    
    
]