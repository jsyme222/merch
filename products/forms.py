#merch/products/form.py

from django import forms

from .models import Vender, VenderMerchandise

class AddVenderMerchandiseForm(forms.Form):
	"""
	Form to add VenderMerchandise 
	to products list
	"""
	vender = forms.ModelChoiceField(
		queryset=Vender.objects.all(),
		help_text='<br><a href="#">Add Vender</a>',
		)

	SKU = forms.CharField(
		max_length=100, 
		label='SKU',
	)

	title = forms.CharField(
		max_length=250, 
		required=False,
	)
	wholesale = forms.DecimalField(
		max_digits=6, 
		decimal_places=2,
		required=False,
		label='Wholesale Cost',
	)

	resale = forms.DecimalField(
		max_digits=6, 
		decimal_places=2,
		required=False, 
		label='Suggested Retail',
	)
	
	img = forms.ImageField(
		required=False,
	)

	QTY = forms.IntegerField(
		required=False,
		label='Quantity in inventory',
	)

	on_floor = forms.IntegerField(
		required=False,
		label='Selling',
	)

	online_info = forms.BooleanField(
		help_text='*If selected the information for the product will be \
		gathered from the merchants website if available',
		required=False,
	)