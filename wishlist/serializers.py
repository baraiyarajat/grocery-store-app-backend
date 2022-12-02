from rest_framework import serializers
from .models import WishlistProduct
from warehouse_product.serializers import WarehouseProductSerializer


class WishlistSerializer(serializers.ModelSerializer):
    warehouse_product = WarehouseProductSerializer()

    class Meta:
        model = WishlistProduct
        fields = ('id', 'warehouse_product', 'date_added')
