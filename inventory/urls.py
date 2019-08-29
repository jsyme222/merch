#merch/main/urls.py
from django.urls import path, include

from . import views
from .views import InventoryListView

urlpatterns = [
	path('', InventoryListView.as_view(), name='inventory.index'),
	path('<str:inventory>/', InventoryListView.as_view(), name='inventory.index'),
]