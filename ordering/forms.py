#merch/inventory/forms.py

from django import forms

from .models import VenderReceipt
from products.models import Vender

class VenderReceiptUploadForm(forms.Form):
	"""
	Form to upload
	VenderReceipt
	"""
	vender = forms.ModelChoiceField(
		queryset=Vender.objects.all(),
		help_text='<br><a href="#">Add Vender</a><br>',
		required=False, 
	)

	order_number = forms.CharField(
		max_length=100, 
		label='Order Number',
		required=False, 
	)

	order_date = forms.DateTimeField(
		label='Order Date',
		required=False, 
	)

	order_total = forms.DecimalField(
		max_digits=7, 
		decimal_places=2,
		required=False,
		label='Order Total',
	)

	shipping_cost = forms.DecimalField(
		max_digits=6, 
		decimal_places=2,
		required=False, 
		label='Shipping Cost',
	)
	
	receipt = forms.FileField(
	)