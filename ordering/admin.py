from django.contrib import admin

from .models import VenderReceipt

# Register your models here.

@admin.register(VenderReceipt)
class VenderReceiptAdmin(admin.ModelAdmin):
	pass