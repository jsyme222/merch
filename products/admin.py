from django.contrib import admin

from .models import Merchant, Product

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
	pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	pass