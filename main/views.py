#merch/main/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User

from products.models import Merchandise

class InventoryListView(ListView):
	"""
	View of inventory for 
	logged in user
	"""
	def get(self, request):
		context = {}
		model = Merchandise.objects.filter(seller=request.user)
		context_object_name = 'products'
		context['products'] = model
		context['product_count'] = len(model)
		return render(request, 'main/inventory.html', context)