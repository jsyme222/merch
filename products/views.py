#merch/products/views.py

from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User

from .models import Vender, Merchandise, VenderMerchandise

from .forms import AddVenderMerchandiseForm

def vender_merchandise_add(request):
	"""
	form to add products
	to product list
	"""
	if request.method == 'POST':
		print('Post request')
		form = AddVenderMerchandiseForm(request.POST)

		if form.is_valid():
			print('Form is valid')
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

			product = VenderMerchandise.objects.create(
				seller=seller,
				vender=vender,
				SKU=SKU,
				title=title,
				wholesale=wholesale,
				img=img,
				QTY=QTY,
				online_info=online_info,
				)

			print('Created Object')

			return redirect('main.index')
		else:
			print('Not valid')

	else:
		print('get request')
		form = AddVenderMerchandiseForm()

	context = {
		'form' : form,
		'venders' : Vender.objects.all(),
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