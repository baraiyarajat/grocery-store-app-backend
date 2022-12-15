from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'warehouse', 'address', 'city', 'status', 'payment_method', 'cart_amount', 'delivery_fee',
                  'final_amount', 'total_items', 'created_date', 'delivery_date', 'delivery_time', 'payment_completed',
                  'formatted_order_status')
