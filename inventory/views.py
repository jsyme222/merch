from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from products.models import Merchandise

from main.views import product_info

class InventoryListView(ListView):
	"""
	View of inventory for 
	logged in user
	"""
	paginate_by = 25
	
	def get(self, request, inventory='full-inventory'):
		context = {}
		model = Merchandise.objects.filter(seller=request.user)

		if inventory != 'full-inventory':
			if inventory == 'selling-inventory':
				context['products_selling'] = model.filter(on_floor__gte=1)
		else:
			context['products'] = model
			
		return render(request, 'inventory/index.html', context)