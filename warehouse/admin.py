from django.contrib import admin
from .models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Warehouse, WarehouseAdmin)
