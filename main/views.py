#merch/main/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User

from products.models import Merchandise
from user.models import SellerStats

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
		seller_stats = SellerStats.objects.get(seller=request.user)
		seller_stats.update()

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

		def ave_product_selling(floor, total):
			dec = floor / total
			ave = dec * 100
			return ave

		inventory = get_inventory_info()
		context['product_count'] = seller_stats.inventory_qty
		context['on_floor_count'] = seller_stats.on_floor_qty
		if inventory['product_count'] > 0:
			context['selling_average'] = round(ave_product_selling(inventory['on_floor_count'], inventory['product_count']))
		context['invested'] = inventory['invested']
		
		return render(request, 'main/index.html', context)
