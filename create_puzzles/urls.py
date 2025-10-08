from django.urls import path,include
from . import views,level_views
app_name = 'create_puzzles'

urlpatterns = [
    path('', views.puzzle_list, name='item-list'),
    path('create/', views.puzzle_create, name='item-create'),
    path('update/<int:pk>/', views.puzzle_update, name='item-update'),
    path('delete/<int:pk>/', views.puzzle_delete, name='item-delete'),
    path('confirm_delete/<int:pk>/', views.puzzle_confirm_delete, name='item-confirm-delete'),
   
   
    path('puzzleLevelTable/',views.puzzle_level_list,name='level-item-list'),
    
    path('leveles/',level_views.levels_list,name='levels-list'),
    
    
    
]