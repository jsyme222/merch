#merch/ordering/models.py
import os

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from products.models import Vender, VenderMerchandise

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
		path = 'media/reciepts/{}'.format(self.seller)
		if not os.path.exists(path):
			os.mkdir(path)
		file = str(file).replace(' ','_')
		return 'reciepts/{}/{}'.format(self.seller, file)

	reciept = models.FileField(upload_to=get_upload_location)

	def add_to_inventory(self, reciept):
		for item in reciept.items():
			sku = item[1]['sku']
			name = item[1]['name']
			qty = item[1]['qty']
			price = item[1]['price']
			product = VenderMerchandise.objects.create(
				seller=self.seller,
				vender=self.vender,
				SKU=sku,
				title=name,
				wholesale=price,
				QTY=qty,
				)
			product.save()
			print('Created:{}'.format(name))

	def scrape_reciept(self, reciept):
		if str(reciept).endswith('.pdf'):
			errors = []
			from PyPDF2 import PdfFileReader
			print(reciept)

			with open(reciept, 'rb') as f:
				pdf = PdfFileReader(f)
				page = pdf.getPage(0)
				text = page.extractText()
				print(text)
			
			def get_label(text, start, end):
				start = text.find(start)
				label_start = text.find('\n', start)
				label_end = text.find(end)
				label = text[label_start:label_end]
				label_list=label.split('\n')
				label_list.pop(0)
				label_list.pop(-1)
				print(label_list)
				return label_list

			sku_list = get_label(text, 'Item', 'Item Name')
			if 'Qty Ordered' in text:
				name_list = get_label(text, 'Item Name', 'Qty')
				qty_list = get_label(text, 'Qty', 'Units')
			else:
				name_list = get_label(text, 'Item Name', 'Quantity')
				qty_list = get_label(text, 'Quantity', 'Units')
			if 'Rate' in text:
				price_list = get_label(text, 'Rate', 'Amount')
			else:
				price_list = get_label(text, 'Price', 'Extended')


			item_lists = { 'sku' : sku_list, 'name' : name_list, 'qty' : qty_list, 'price' : price_list}

			final_items = {}

			x = 0
			count = len(item_lists['sku'])

			while x < count:
				final_items[x] = {
				'sku':sku_list[x], 
				'name':name_list[x], 
				'qty':qty_list[x], 
				'price':price_list[x],
				}
				x += 1

			self.add_to_inventory(final_items)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		reciept = 'media/{}'.format(self.reciept)
		self.scrape_reciept(reciept)