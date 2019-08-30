#merch/products/views.py

from django.utils import timezone
from django.utils.html import mark_safe
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Vender, Merchandise, VenderMerchandise, SellerMerchandise

from .forms import AddVenderMerchandiseForm

def vender_merchandise_add(request):
	"""
	form to add products
	to product list
	"""
	if request.method == 'POST':
		form = AddVenderMerchandiseForm(request.POST)

		if form.is_valid():
			seller = request.user
			vender = form.cleaned_data['vender']
			SKU = form.cleaned_data['SKU']
			title = form.cleaned_data['title']
			if form.cleaned_data['wholesale']:
				wholesale = form.cleaned_data['wholesale']
			else:
				wholesale = 0
			img = form.cleaned_data['img']
			QTY = form.cleaned_data['QTY']
			if form.cleaned_data['online_info']:
				online_info = True
			else:
				online_info = False 
			on_floor = form.cleaned_data['on_floor']

			product = VenderMerchandise.objects.create(
				seller=seller,
				vender=vender,
				SKU=SKU,
				title=title,
				wholesale=wholesale,
				img=img,
				QTY=QTY,
				on_floor=on_floor,
				online_info=online_info,
				)

			return redirect('/products/vender/{}'.format(product.pk))
		else:
			print('Not valid')

	else:
		form = AddVenderMerchandiseForm()

	context = {
		'form' : form,
	}
	return render(request, 'products/vendermerchandise_form.html', context)

class VenderMerchandiseDetail(DetailView):
	"""
	View of individual
	vender product details
	"""
	model = VenderMerchandise

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class SellerMerchandiseDetail(DetailView):
	"""
	View of indiviual
	seller product details
	"""
	model = SellerMerchandise

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class VenderMerchandiseUpdate(UpdateView):
	"""
	Update VenderMerchandise objects
	"""
	fields = ['vender', 'SKU', 'title', 'wholesale', 'resale', 'img', 'QTY', 'on_floor', 'online_info',]

	def get_queryset(self):
		self.user = self.request.user
		return VenderMerchandise.objects.filter(seller=self.user)

def update_inventory(request, pk, qty):
	if request.is_ajax():
		product_to_update = Merchandise.objects.get(pk=pk)
		product_to_update.QTY = qty
		product_to_update.save()
		print('product updated')
		return HttpResponse('Inventory Item: {}\nNew inventory amount: {}'.format(product_to_update.title, product_to_update.QTY))
	else:
		return HttpResponse('Sorry, not available')