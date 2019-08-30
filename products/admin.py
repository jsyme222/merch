#merch/products/admin.py

from django.contrib import admin

from .models import Vender, Expense, Merchandise, VenderMerchandise, SellerMerchandise

@admin.register(Vender)
class VenderAdmin(admin.ModelAdmin):
	pass

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	pass

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
	readonly_fields = ['profit', 'image_tag',]

@admin.register(VenderMerchandise)
class VenderMerchandise(admin.ModelAdmin):
	pass

@admin.register(SellerMerchandise)
class SellerMerchandiseAdmin(admin.ModelAdmin):
	pass