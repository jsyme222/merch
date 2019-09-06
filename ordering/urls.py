#merch/main/urls.py
from django.conf import settings
from django.urls import path, include

from . import views

urlpatterns = [
	path('add/', views.vender_merchandise_receipt_add, name='ordering.receipt_add'),
]