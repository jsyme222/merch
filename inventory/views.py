from django.shortcuts import render
from django.views.generic import ListView

from products.models import Merchandise

from main.views import product_info

class InventoryListView(ListView):
	"""
	View of inventory for 
	logged in user
	"""
	paginate_by = 25
	
	def get(self, request):
		context = {}
		model = Merchandise.objects.filter(seller=request.user)
		context['products'] = model
		print(context['products'])
		return render(request, 'inventory/index.html', context)