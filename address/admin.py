from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_type', 'pincode', 'city')


admin.site.register(Address, AddressAdmin)
