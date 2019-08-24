from django.contrib import admin

from .models import Vender, Merchandise, VenderMerchandise

@admin.register(Vender)
class VenderAdmin(admin.ModelAdmin):
	pass

@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
	readonly_fields = ['resale']

@admin.register(VenderMerchandise)
class VenderMerchandise(admin.ModelAdmin):
	pass