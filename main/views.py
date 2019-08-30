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

		def get_product_count():
			product_count = 0
			for product in products:
				if product.QTY:
					qty = product.QTY
					product_count += qty
			return product_count

		def get_on_floor_count():
			on_floor = products.filter(on_floor__gte=1)
			final_count = 0
			for item in on_floor:
				on_floor = item.on_floor
				final_count += on_floor
			return final_count

		context['product_count'] = get_product_count()
		context['on_floor_count'] = get_on_floor_count()

		return render(request, 'main/index.html', context)
