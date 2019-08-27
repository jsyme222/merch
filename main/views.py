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
		context['products'] = product_info(request)
		return render(request, 'main/index.html', context)
