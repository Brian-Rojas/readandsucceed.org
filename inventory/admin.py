from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'amount', 'barcode']
	search_fields = ['title', 'barcode']

admin.site.register(Item, ItemAdmin)