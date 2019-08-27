#merch/main/urls.py
from django.conf import settings
from django.urls import path, include

from . import views
from .views import MainIndex

urlpatterns = [
	path('', MainIndex.as_view(), name='main.index'),
]