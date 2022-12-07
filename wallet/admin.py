from django.contrib import admin
from .models import Wallet


class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'credit', 'cashback_balance', 'modified_date')


admin.site.register(Wallet, WalletAdmin)
