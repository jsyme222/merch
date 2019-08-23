#merch/products/models.py
import os
import requests
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

from django.db import models
from django.conf import settings

"""
Individual product item information
as well as merchant info. 
'Product' models are used in building 
'Inventory' and 'Ordering' models.
"""

class Merchant(models.Model):
	"""
	Merchant information
	"""
	merchant = models.CharField(max_length=150, blank=False, null=True)
	contact_email = models.CharField(max_length=100, null=True, blank=True)

	account_user = models.CharField(max_length=150, null=True, blank=True)
	account_pass = models.CharField(max_length=150, null=True, blank=True)

	url = models.CharField(max_length=550, null=True, blank=True)

	def __str__(self):
		return self.merchant

class Product(models.Model):
	"""
	Parent product item class
	"""
	merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
	SKU = models.CharField(max_length=100, unique=True)
	title = models.CharField(max_length=250, unique=True, null=True, blank=True)
	wholesale = models.DecimalField(max_digits=6, decimal_places=2)
	resale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, editable=False)
	profit = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, editable=False)
	QTY = models.IntegerField(blank=True, null=True)

	get_online_img = models.BooleanField(default=False)
	img = models.ImageField(blank=True, null=True, default='')

	def __str__(self):
		return self.title

	def get_img_url(self):
		page = requests.get(self.merchant.url + self.SKU)
		html = page.text
		soup = BeautifulSoup(html, 'html.parser')
		img = soup.find('img', attrs={'id':re.compile(r'^ProductPic')})
		local_url = img['src']
		file_name = local_url.split('/')[-1]
		domain = self.merchant.url.split('/')
		download_url = '/'.join(domain[:3]) + local_url 

		def get_location(self):
			return 'media/products/{}'.format(file_name)

		try:
			data = urlopen(download_url).read()
			output = open(get_location(self), 'wb')
			print('opened file')
			output.write(data)
			print('file written')
			output.close()
			print('file closed')

			final = get_location(self).split('/')
			final_url = '/'.join(final[1:])
			return final_url

		except:
			print('Failed!!!!!!!!!!')
			return

	def save(self, *args, **kwargs):
		if self.get_online_img:
			self.img = self.get_img_url()
		super(Product, self).save(*args, **kwargs)