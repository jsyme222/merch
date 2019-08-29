#merch/products/form.py

from django import forms

from .models import Vender, VenderMerchandise

class AddVenderMerchandiseForm(forms.Form):
	"""
	Form to add VenderMerchandise 
	to products list
	"""
	vender = forms.ModelChoiceField(queryset=Vender.objects.all())

	SKU = forms.CharField(max_length=100)

	title = forms.CharField(
		max_length=250, 
		required=False,
	)
	wholesale = forms.DecimalField(
		max_digits=6, 
		decimal_places=2,
		required=False,
	)

	resale = forms.DecimalField(
		max_digits=6, 
		decimal_places=2,
		required=False, 
	)
	
	img = forms.ImageField(
		required=False,
	)

	QTY = forms.IntegerField(
		required=False,
	)

	online_info = forms.BooleanField(
		help_text='*If selected the information for the product will be \
		gathered from the merchants website if available',
		required=False,
	)