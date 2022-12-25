from rest_framework import serializers
from .models import Address
from warehouse.serializers import WarehouseSerializer

class AddressSerializer(serializers.ModelSerializer):

    city = WarehouseSerializer()
    class Meta:
        model = Address
        fields = ('id', 'address_type', 'address_line_1', 'address_line_2', 'pincode', 'city')