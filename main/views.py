#merch/main/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User

from products.models import Merchandise

def product_info(request):
	"""
	Get seller merchandise info
	"""
	products = Merchandise.objects.filter(seller=request.user)
	return products

class MainIndex(View):
	"""
	Main Landing Page of app
	"""
	def get(self, request):
		context = {}
		products = product_info(request)

		def get_inventory_info():
			inv_info = {}
			product_count = 0
			invested = 0
			on_floor_count = 0

			for product in products:
				if product.QTY:
					qty = product.QTY
					product_count += qty
				if product.wholesale:
					amount = product.wholesale
					invested += amount
				if product.on_floor >= 1:
					on_floor = product.on_floor
					on_floor_count += on_floor

			inv_info['product_count'] = product_count
			inv_info['invested'] = invested
			inv_info['on_floor_count'] = on_floor_count

			return inv_info

		def get_on_floor_count():
			on_floor = products.filter(on_floor__gte=1)
			final_count = 0
			for item in on_floor:
				on_floor = item.on_floor
				final_count += on_floor
			return final_count

		def ave_product_selling(floor, total):
			dec = floor / total
			ave = dec * 100
			return ave

		inventory = get_inventory_info()
		context['product_count'] = inventory['product_count']
		context['on_floor_count'] = inventory['on_floor_count']
		if inventory['product_count'] > 0:
			context['selling_average'] = round(ave_product_selling(inventory['on_floor_count'], inventory['product_count']))
		context['invested'] = inventory['invested']
		
		return render(request, 'main/index.html', context)
