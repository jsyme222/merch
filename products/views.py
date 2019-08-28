from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Merchandise, VenderMerchandise

class VenderMerchandiseCreate(CreateView):
	model = VenderMerchandise
	fields = ['vender', 'SKU', 'wholesale', 'QTY',]
