#merch/main/urls.py
from django.conf import settings
from django.urls import path, include

from . import views
from .views import InventoryListView

urlpatterns = [
    path('inventory/', InventoryListView.as_view(), name='main.inventory'),
]