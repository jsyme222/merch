#merch/main/urls.py
from django.conf import settings
from django.urls import path, include

from . import views
from .views import VenderMerchandiseDetail, VenderMerchandiseUpdate

urlpatterns = [
	path('add/', views.vender_merchandise_add, name='products.add'),
	path('<int:pk>/', VenderMerchandiseDetail.as_view(), name='products.detail'),
	path('update/<int:pk>/', VenderMerchandiseUpdate.as_view(), name='products.update'),
]