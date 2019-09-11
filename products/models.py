#merch/products/models.py
import os
import requests
import re
from urllib.error import URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
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

class Expense(models.Model):
	"""
	Individual expense 
	model
	"""
	expense_title = models.CharField(max_length=250, blank=False)
	unit_price = models.DecimalField(
		max_digits=6, 
		decimal_places=2, 
	)

class Merchandise(models.Model):
	"""
	Parent product item class
	"""
	class Meta:
		verbose_name_plural = 'Merchandise'

	seller = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		null=True, 
		on_delete=models.SET_NULL,
	)
	
	class_name = models.CharField(
		max_length=250, 
		null=True, 
		blank=True,
		default='',
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
		default=0,
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

	on_floor = models.IntegerField(
		verbose_name='Selling',		
		blank=True,
		null=True,
		default=0,
	)

	created_on = models.DateTimeField(auto_now_add=True)

	def image_tag(self):
		return mark_safe('<img src="/media/%s" width="200" height="150" class="bordered" />' % (self.img))

	image_tag.short_description = 'Image'

	def record_sale(self, qty_sold, selling_price):
		errors = {}
		context = {}
		if self.QTY and self.QTY >= 1:
			self.QTY -= qty_sold
			context['QTY'] = self.QTY
		else:
			errors['qty'] = 'Quantity unavailable for sale'

		if self.on_floor and self.on_floor >= 1:
			self.on_floor -= qty_sold
			context['on_floor'] = self.on_floor
		else:
			errors['on_floor'] = 'On floor quantity unavailable for sale'

		if self.profit and self.on_floor >=1:
			self.profit += selling_price
			context['profit'] = self.profit
		if errors:
			for error in errors.keys():
				print('{}: {}'.format(error, errors[error]))
			return errors
		else:
			for i in context.keys():
				print('{}: {}'.format(i, context[i]))
			return context

	def __str__(self):
		if not self.title:
			return str(self.SKU)
		return self.title + ' => ' + self.seller.username

	def get_absolute_url(self):
		return "/products/{}/{}/".format(self.class_name, self.pk)

class SellerMerchandise(Merchandise):
	"""
	Products prepared or
	created by the seller
	"""
	class Meta:
		verbose_name_plural = 'Seller Merchandise'

	expenses = models.ManyToManyField(Expense, blank=True,)

	def save(self, *args, **kwargs):
		self.class_name = 'seller'
		super(Merchandise, self).save(*args, **kwargs)

class VenderMerchandise(Merchandise):
	"""
	Products ordered wholesale from vendors
	"""
	class Meta:
		verbose_name_plural = 'Vender Merchandise'

	vender = models.ForeignKey(
		Vender, 
		null=True,
		on_delete=models.SET_NULL,
	)

	online_info = models.BooleanField(
		verbose_name='Get info from website?*',
		help_text='*If selected the information for the product will be \
		gathered from the merchants website if available',
		default=False,
	)

	def get_product_info(self):

		product_info = {}
		page = requests.get(self.vender.url + self.SKU)
		if page.status_code == 200:
			try:
				html = page.text
				soup = BeautifulSoup(html, 'html.parser')
				#store_html_copy(self, soup)
				domain = self.vender.url.split('/')

				img = soup.find('img', id=re.compile(r'^Product'))

				def get_image(img):
					local_url = img['src']
					file_name = local_url.split('/')[-1]
					download_url = '/'.join(domain[:3]) + local_url 

					try:
						data = urlopen(download_url).read()
						vender_dir = 'media/products/{}'.format(self.vender.vender)
						if not os.path.exists(vender_dir):
							os.mkdir(vender_dir)
						output = open(vender_dir + '/' + file_name, 'wb')
						output.write(data)
						output.close()

						final_url = 'products/{}/{}'.format(self.vender.vender, file_name)
						return final_url

					except URLError:
						print('Error in {}'.format(__name__))

					product_info['title'] = img['alt']
					product_info['image'] = get_image(img)
			
			except:
				product_info['title'] = 'None'
				product_info['image'] = 'None'
				product_info['errors'] = 'Product Unavailable'

		return product_info

	def check_SKU(self):
		try:
			product = Merchandise.objects.get(SKU=self.SKU)
			return product
		except Merchandise.DoesNotExist:
			return False

	def save(self, *args, **kwargs):
		in_inventory = self.check_SKU()
		if in_inventory:
			if in_inventory.seller == self.seller:
				in_inventory.QTY += self.QTY
				in_inventory.on_floor += self.on_floor
				in_inventory.save()
				return
		if self.online_info:
				info = self.get_product_info()
				self.img = info['image']
				self.title = info['title']
				if 'errors' in info.keys():
					print('Unable to get online info: {}'.format(info['errors']))
		self.online_info = False
		self.class_name = 'vender'
		if not self.resale:
			self.resale = self.wholesale * 2
		super(Merchandise, self).save(*args, **kwargs)
