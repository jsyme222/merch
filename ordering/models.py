#merch/ordering/models.py

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from products.models import Vender

class VenderReciept(models.Model):
	"""
	Uploadable reciept that 
	inventory will be added
	to inventory
	"""
	class Meta:
		verbose_name_plural='Reciepts'

	seller = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		null=True, 
		on_delete=models.SET_NULL
		)

	vender = models.ForeignKey(
		Vender, 
		null=True, 
		blank=True, 
		on_delete=models.SET_NULL
		)

	order_number = models.CharField(
		max_length=100, 
		null=True, 
		blank=True
		)

	order_date = models.DateTimeField(
		null=True, 
		blank=True
		)

	order_total = models.DecimalField(
		max_digits=6, 
		decimal_places=2,
		null=True,
		blank=True,
	)

	shipping_cost = models.DecimalField(
		max_digits=6, 
		decimal_places=2,
		null=True,
		blank=True,
	)

	def get_upload_location(self, file):
		return 'reciepts/{}/{}'.format(self.seller, file)

	reciept = models.FileField(upload_to=get_upload_location)