#merch/main/urls.py
from django.conf import settings
from django.urls import path, include

from . import views
from .views import VenderMerchandiseDetail, SellerMerchandiseDetail, VenderMerchandiseUpdate

urlpatterns = [
	path('add/', views.vender_merchandise_add, name='products.add'),
	path('vender/<int:pk>/', VenderMerchandiseDetail.as_view(), name='vender_product.detail'),
	path('seller/<int:pk>/', SellerMerchandiseDetail.as_view(), name='seller_product.detail'),
	path('update/<int:pk>/', VenderMerchandiseUpdate.as_view(), name='products.update'),
	path('ajax/update-inventory/<int:pk>/<int:qty>/', views.update_inventory, name='products.update_inventory'),
]