from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_date', 'warehouse')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'quantity')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
