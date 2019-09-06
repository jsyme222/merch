#merch/main/urls.py
from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.inventory_index, name='inventory.index'),
	path('<str:inventory>/', views.inventory_index, name='inventory.index'),
	path('?page=<int:page>/', views.inventory_index, name='inventory.index'),
	path('<str:inventory>/?page=<int:page>', views.inventory_index, name='inventory.index'),
]