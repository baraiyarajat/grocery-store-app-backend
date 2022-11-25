from django.contrib import admin
from .models import Warehouse, SelectedWarehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Warehouse, WarehouseAdmin)


class SelectedWarehouseAdmin(admin.ModelAdmin):
    list_display = ('user', 'warehouse')


admin.site.register(SelectedWarehouse, SelectedWarehouseAdmin)
