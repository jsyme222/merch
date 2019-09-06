from django.shortcuts import render, redirect

from .models import VenderReceipt
from .forms import VenderReceiptUploadForm
# Create your views here.

def vender_merchandise_receipt_add(request):
	"""
	form to add products
	to product list
	"""
	if request.method == 'POST':
		form = VenderReceiptUploadForm(request.POST, request.FILES)

		if form.is_valid():
			seller = request.user
			vender = form.cleaned_data['vender']
			order_number = form.cleaned_data['order_number']
			order_date = form.cleaned_data['order_date']
			order_total = form.cleaned_data['order_total']
			shipping_cost = form.cleaned_data['shipping_cost']
			receipt = form.cleaned_data['receipt']

			receipt = VenderReceipt.objects.create(
				seller=seller,
				vender=vender,
				order_number=order_number,
				order_total=order_total,
				order_date=order_date,
				shipping_cost=shipping_cost,
				receipt=receipt,
				)

			return redirect('/inventory/')
		else:
			print('Not valid')

	else:
		form = VenderReceiptUploadForm()

	context = {
		'form' : form,
	}
	return render(request, 'ordering/venderreceipt_form.html', context)