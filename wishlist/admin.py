from django.contrib import admin
from .models import WishlistProduct


class WishlistProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'warehouse_product', 'date_added']


admin.site.register(WishlistProduct, WishlistProductAdmin)
