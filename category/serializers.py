from rest_framework import serializers
from .models import Category
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'image')
        # fields = ('id', 'name', 'slug', 'category_image')

    def get_image_url(self, obj):
        return   obj.image.url