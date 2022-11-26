from rest_framework import serializers
from .models import WarehouseProduct
from product.serializers import ProductSerializer


class WarehouseProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WarehouseProduct
        fields = ('id', 'warehouse', 'product', 'price', 'stock', 'discount_rate', 'created_date', 'modified_date')
