from rest_framework import serializers
from .models import CartProduct
from warehouse_product.serializers import WarehouseProductSerializer


class CartProductSerializer(serializers.ModelSerializer):
    warehouse_product = WarehouseProductSerializer()

    class Meta:
        model = CartProduct
        fields = ('id', 'warehouse_product', 'quantity', 'modified_date')
