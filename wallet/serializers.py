from .models import Wallet
from rest_framework import serializers


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('user', 'credit', 'cashback_balance', 'modified_date', 'formatted_modified_date')
