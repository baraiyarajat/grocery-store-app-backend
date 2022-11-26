from django.shortcuts import render
from rest_framework.views import APIView
from .models import WarehouseProduct
from category.models import Category
from .serializers import WarehouseProductSerializer
from rest_framework.response import Response

class WarehouseProductListView(APIView):

    def get(self, request):
        category_slug = request.GET['category_slug']
        warehouse_id = request.GET['warehouse_id']
        category_object = Category.objects.get(slug=category_slug)

        warehouse_product_objects = WarehouseProduct.objects.filter(product__category=category_object,
                                                                    warehouse__id=warehouse_id)
        warehouse_product_serializer = WarehouseProductSerializer(warehouse_product_objects, many=True)
        return Response(warehouse_product_serializer.data, status=200)
