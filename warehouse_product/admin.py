from django.contrib import admin
from .models import WarehouseProduct


class WarehouseProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'stock', 'price', 'modified_date')


admin.site.register(WarehouseProduct, WarehouseProductAdmin)
