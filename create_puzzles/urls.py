from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('list/',views.puzzle_list,name='puzzle-list'),
    path('create/',views.puzzle_create,name='puzzle-create'),
    path('update/<int:pk>/',views.puzzle_update,name='puzzle-update'),
    path('delete/<int:pk>/',views.puzzle_delete,name='puzzle-delete'),
]
