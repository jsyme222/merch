from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from products.models import Merchandise

from main.views import product_info

def inventory_index(request, inventory='full-inventory'):
	context = {}
	model = Merchandise.objects.filter(seller=request.user)
	page = request.GET.get('page', 1)
	group_details = {
		'title' : 'All',
		'color' : '#099a8c',
	}

	def get_queryset(inventory):
		if inventory == 'selling-inventory':
			group_details['title'] = 'Selling'
			group_details['color'] = '#0082d4'
			context['is_selling'] = True
			queryset = model.filter(on_floor__gte=1)
		elif inventory == 'seller':
			group_details['title'] = 'Seller'
			group_details['color'] = '#1b3148'
			queryset = model.filter(class_name='seller')
		elif inventory == 'vender':
			group_details['title'] = 'Vender'
			group_details['color'] = '#faa652'
			queryset = model.filter(class_name='vender')
		else:
			queryset = model
		return queryset

	queryset = get_queryset(inventory)
	paginator = Paginator(queryset, 15)

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context['products'] = products
	context['paginator'] = paginator
	context['group_details'] = group_details

	return render(request, 'inventory/index.html', context)
