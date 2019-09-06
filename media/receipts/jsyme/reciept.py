first = 'Credit_Card_Invoice_Invoice_CS2085_1486594339111_mxWPOKd.pdf'
second = 'Sales_Order_SO10014575_1497310359224.pdf'

class VenderMerchandise:

	def __init__(self):

		self.SKU = ''

		self.title = ''

class receipt:

	def __init__(self, path):
		self.path = path
		self.prods = {}

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

		return self.prods

	def save(self):
		for item in self.products().values():
			prod = VenderMerchandise()
			prod.title = item[1]
			prod.SKU = item[0]
		print('Saved Products')

receipt1 = receipt(first)
receipt1.save()
