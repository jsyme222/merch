#merch/inventory/admin.py

from django.contrib import admin

from .models import SellerInventory

@admin.register(SellerInventory)
class SellerInventoryAdmin(admin.ModelAdmin):
	read_only_fields = ['inventory',]
