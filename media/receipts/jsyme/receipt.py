first = 'Credit_Card_Invoice_Invoice_CS2085_1486594339111_mxWPOKd.pdf'
second = 'Sales_Order_SO10014575_1497310359224.pdf'

class VenderMerchandise:

	def __init__(self):

		self.SKU = ''

		self.title = ''

class PdfReceipt:

	def __init__(self, path):
		self.path = path
		self.prods = {}

		with open(self.path, 'rb') as f:
			from PyPDF2 import PdfFileReader
			pdf = PdfFileReader(f)
			page = pdf.getPage(0)
			self.text = page.extractText()	
			self.listed_items = self.text.split('\n')

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

		return self.prods

	def save(self):
		for item in self.products().values():
			prod = VenderMerchandise()
			prod.title = item[1]
			prod.SKU = item[0]
		print('Saved Products')

class EmlReceipt:

	def __init__(self, path):
		import eml_parser
		self.path = path
		self.prods = {}

		with open(self.path, 'rb') as f:
			raw_email = f.read()
			raw_email = str(raw_email).replace('\\r', '')
			raw_email = raw_email.split('\\n')
			self.listed = raw_email

	def get_order_date(self):
		f = self.listed
		for x in f:
			if 'Order Date:' in x and '</' not in x:
				x = x.split(' ')
				order_date = x[2:4]
				order_date = ' '.join(order_date)
				print(order_date)
				return order_date

	def products(self):	

		def rid_stragglers(objs):
			straggle_free = []
			for obj in objs:
				if len(obj) >= 4:
					straggle_free.append(obj)
				else:
					straggle_free[-1] += obj
			return straggle_free

		f = self.listed
		for x in f:
			if 'SKU: ' in x:
				prods_start = f.index(x)+1
			if 'Order Notes:' in x and '</' not in x:
				prods_end = f.index(x)
		prods = f[prods_start:prods_end]
		for x in prods:
			if x.startswith('*') or len(x) <= 5:
				prods.remove(x)
		skus = []
		for prod in prods:
			if len(prod) <= 6:
				continue
			else:
				splits = prod.split(' ')
				splits = rid_stragglers(splits)
				print(splits)
				if len(splits[0]) < 5:
					pass
				else:
					skus.append(splits[0])
		print(skus)

e = EmlReceipt('foreside1.eml')
e.products()
