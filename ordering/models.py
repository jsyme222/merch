#merch/ordering/models.py
import os

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from products.models import Vender, VenderMerchandise
class PdfReceipt:

	def __init__(self, path, seller, vender):
		self.path = path
		self.prods = {}
		self.seller = seller
		self.vender = vender

		with open(self.path, 'rb') as f:
			from PyPDF2 import PdfFileReader
			pdf = PdfFileReader(f)
			page = pdf.getPage(0)
			self.text = page.extractText()	
			self.listed_items = self.text.split('\n')
			print('receipt {} added'.format(pdf))

	def products(self):

		def get_list(self, start, end, text):
			start_index = self.listed_items.index(start)
			end_index = self.listed_items.index(end)
			listed = []
			for i in self.listed_items[start_index+1:end_index]:
				listed.append(i)
			return listed

		def rid_stragglers(names):
			straggle_free = []
			for name in names:
				l = len(name.replace(' ',''))
				if l > 10:
					straggle_free.append(name)
				elif l > 4:
					straggle_free[-1] += name
			return straggle_free

		items = self.listed_items	
		skus = get_list(self, 'Item #', 'Item Name', items)

		if 'Qty' not in self.text:
			names = get_list(self, 'Item Name', 'Quantity', items)
			qty = get_list(self, 'Quantity', 'Units', items)
			price = get_list(self, 'Rate', 'Amount', items)
		else:
			names = get_list(self, 'Item Name', 'Qty Ordered', items)
			qty = get_list(self, 'Qty Ordered', 'Units', items)
			price = get_list(self, 'Item Price', 'Extended A...', items)
		
		if len(names) > len(skus):
			names = rid_stragglers(names)
		if len(names) > len(skus):
			names = rid_stragglers(names)

		while len(self.prods.keys()) < len(skus):
			x = len(self.prods.keys())
			self.prods[x] = (skus[x], names[x], qty[x], price[x])

		#for i in self.prods.values():
		#	print(i[3])
		return self.prods

	def save(self):
		for item in self.products().values():
			sku = item[0]
			name = item[1]
			qty = item[2]
			price = item[3]
			product = VenderMerchandise.objects.create(
				seller=self.seller,
				vender=self.vender,
				SKU=sku,
				title=name,
				wholesale=float(price),
				QTY=qty,
				)
			product.save()

class VenderReceipt(models.Model):
	"""
	Uploadable receipt that 
	inventory will be added
	to inventory
	"""
	class Meta:
		verbose_name_plural='Receipts'

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
		path = 'media/receipts/{}'.format(self.seller)
		if not os.path.exists(path):
			os.mkdir(path)
		file = str(file).replace(' ','_')
		return 'receipts/{}/{}'.format(self.seller, file)

	receipt = models.FileField(upload_to=get_upload_location)
			
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		receipt_url = 'media/{}'.format(self.receipt)
		if receipt_url.endswith('pdf'):
			receipt = PdfReceipt(receipt_url, self.seller, self.vender)
		receipt.save()