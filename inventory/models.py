#merch/inventory/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from products.models import Merchandise

class SellerInventory(models.Model):
	"""
	Collect all inventory 
	information for logged in 
	User
	"""
	class Meta:
		verbose_name_plural = 'Inventories'

	seller = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		null=True, 
		on_delete=models.SET_NULL
		)

	inventory_title = models.CharField(max_length=250, blank=False, null=True, default='Default')

	products = models.ManyToManyField(Merchandise)
	
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.seller)

	# def save(self, *args, **kwargs):
	# 	super(UserInventory, self).save(*args, **kwargs)

	