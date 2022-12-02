from django.contrib import admin
from .models import CartProduct


class CartProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'warehouse_product', 'quantity', 'modified_date']


admin.site.register(CartProduct,CartProductAdmin)
