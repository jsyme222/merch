#merch/user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from products.models import Merchandise

class CustomUser(AbstractUser):
	pass


class SellerStats(models.Model):

	class Meta:
		verbose_name_plural='Seller Stats'

	seller = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		null=True, 
		on_delete=models.SET_NULL
	)

	title = models.CharField(max_length=150, default='Seller Stats')

	gross_income = models.DecimalField(
		max_digits=6, 
		decimal_places=2,
		null=True,
		blank=True,
		default= 0,
	)

	net_income = models.DecimalField(
		max_digits=6, 
		decimal_places=2,
		null=True,
		blank=True,
		default= 0,
	)

	inventory_qty = models.IntegerField(
		blank=True, 
		default=0,
		null=True,
	)

	on_floor_qty = models.IntegerField(
		blank=True, 
		default=0,
		null=True,
	)

	def update(self):
		try:
			i = Merchandise.objects.filter(seller=self.seller)
			qty = 0
			floor = 0
			for x in i:
				qty += x.QTY
				floor += x.on_floor
			self.inventory_qty = qty
			self.on_floor_qty = floor
		except Merchandise.DoesNotExist:
			print('No merchandise found')
				
	def __str__(self):
		return 'Seller Stats => {}'.format(self.seller)

	def save(self, *args, **kwargs):
		try:
			i = Merchandise.objects.filter(seller=self.seller)
			qty = 0
			floor = 0
			for x in i:
				qty += x.QTY
				floor += x.on_floor
			self.inventory_qty = qty
			self.on_floor_qty = floor
		except Merchandise.DoesNotExist:
			print('No merchandise found')
		super().save(*args, **kwargs)