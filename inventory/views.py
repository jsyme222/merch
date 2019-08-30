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
		class_info = {
			'title' : 'All',
			'color' : '#fffff',
		}

		if inventory != 'full-inventory':

			if inventory == 'selling-inventory':
				model = model.filter(on_floor__gte=1)
				class_info = {
					'title' : 'For Sale',
					'color' : '#0082d4',
				}
				context['products_selling'] = True

			if inventory == 'seller':
				model = model.filter(class_name='seller')
				class_info = {
					'title' : 'Seller',
					'color' : '#1b3148',
				}

			if inventory == 'vender':
				model = model.filter(class_name='vender')
				class_info = {
					'title' : 'Vender',
					'color' : '#faa652',
				}

		context['products'] = model
		context['class_info'] = class_info
		return render(request, 'inventory/index.html', context)