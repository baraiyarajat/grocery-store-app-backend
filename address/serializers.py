from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'address_type', 'address_line_1', 'address_line_2', 'pincode', 'city')