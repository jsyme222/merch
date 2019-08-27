#merch/main/urls.py
from django.conf import settings
from django.urls import path, include

from . import views
from .views import VenderMerchandiseCreate

urlpatterns = [
	path('add/', VenderMerchandiseCreate.as_view(), name='products.add'),
]