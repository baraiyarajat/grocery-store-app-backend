from rest_framework import serializers
from .models import Warehouse, SelectedWarehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id', 'name', 'slug')


class SelectedWarehouseSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer(read_only=True)

    class Meta:
        model = SelectedWarehouse
        fields = ('warehouse',)
