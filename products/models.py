#merch/products/models.py
import os
import requests
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

from django.db import models
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User

"""
Individual product item information
as well as merchant info. 
'Product' models are used in building 
'Inventory' and 'Ordering' models.
"""

class Vender(models.Model):
	"""
	Vendor information
	"""
	vender = models.CharField(max_length=150, blank=False, null=True)
	contact_email = models.CharField(max_length=100, null=True, blank=True)

	account_user = models.CharField(max_length=150, null=True, blank=True)
	account_pass = models.CharField(max_length=150, null=True, blank=True)

	url = models.CharField(max_length=550, null=True, blank=True)
#https://www.foresidehomeandgarden.com/searchadv.aspx?searchterm=

	def __str__(self):
		return self.vender

class Merchandise(models.Model):
	"""
	Parent product item class
	"""
	class Meta:
		verbose_name_plural = 'Merchandise'

	seller = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

	vender = models.ForeignKey(
		Vender, 
		null=True,
		on_delete=models.SET_NULL,
	)

	SKU = models.CharField(
		max_length=100, 
	)

	title = models.CharField(
		max_length=250, 
		null=True, 
		blank=True,
		default='',
	)

	wholesale = models.DecimalField(
		max_digits=6, 
		decimal_places=2,
	)

	resale = models.DecimalField(
		max_digits=6, 
		decimal_places=2, 
		null=True, 
		blank=True, 
		verbose_name='Suggested retail',
	)

	profit = models.DecimalField(
		max_digits=6, 
		decimal_places=2, 
		null=True, 
		blank=True, 
		editable=False,
	)
	
	img = models.ImageField(
		blank=True, 
		null=True, 
		default='',
	)

	QTY = models.IntegerField(
		blank=True, 
		default=0,
		null=True,
		)

	def __str__(self):
		if not self.title:
			return str(self.SKU)
		return self.title



class VenderMerchandise(Merchandise):
	"""
	Products ordered wholesale from vendors
	"""
	class Meta:
		verbose_name_plural = 'Vender Merchandise'

	online_info = models.BooleanField(
		verbose_name='Get info from website?*',
		help_text='*If selected the information for the product will be \
		gathered from the merchants website if available',
		default=False,
	)

	def get_product_info(self):
		product_info = {}
		page = requests.get(self.vender.url + self.SKU)
		print('################' + str(page.status_code))
		html = page.text
		soup = BeautifulSoup(html, 'html.parser')
		domain = self.vender.url.split('/')
		img = soup.find('img', attrs={'id':re.compile(r'^ProductPic')})

		def get_title():
			title = img['alt']
			return title

		def get_image():
			local_url = img['src']
			file_name = local_url.split('/')[-1]
			download_url = '/'.join(domain[:3]) + local_url 

			def get_location():
				return 'media/products/{}'.format(file_name)

			try:
				data = urlopen(download_url).read()
				output = open(get_location(), 'wb')
				output.write(data)
				output.close()

				final = get_location().split('/')
				final_url = '/'.join(final[1:])
				return final_url

			except Exception:
				return 'Error: {}'.format(Exception)

		product_info['title'] = get_title()
		product_info['image'] = get_image()

		return product_info

	def check_SKU(self):
		product = Merchandise.objects.get(SKU=self.SKU)
		if product:
			return True
		return False

	def save(self, *args, **kwargs):
		if self.online_info:
			if not self.check_SKU():
				info = self.get_product_info()
				self.resale = self.wholesale * 2
				if self.online_info:
					self.img = info['image']
					self.title = info['title']
			else:
				product = Merchandise.objects.get(SKU=self.SKU)
				self.title = product.title
				self.wholesale = product.wholesale
				self.resale = product.resale
				self.profit = product.profit
				self.img = product.img
			self.online_info = False
		super(Merchandise, self).save(*args, **kwargs)