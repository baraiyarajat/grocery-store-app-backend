from rest_framework import serializers
from category.serializers import CategorySerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'description', 'benefits', 'how_to_use', 'disclaimer', 'category')
