from django.contrib import admin

from .models import VenderReciept

# Register your models here.

@admin.register(VenderReciept)
class VenderRecieptAdmin(admin.ModelAdmin):
	pass