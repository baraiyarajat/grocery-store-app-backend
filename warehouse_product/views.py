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
                                                                    warehouse__id=warehouse_id).order_by('product__name')
        warehouse_product_serializer = WarehouseProductSerializer(warehouse_product_objects, many=True)
        return Response(warehouse_product_serializer.data, status=200)


class WarehouseProductDetailsView(APIView):

    def get(self, request, product_slug):
        warehouse_id = request.GET["warehouse_id"]
        warehouse_product_object = WarehouseProduct.objects.get(product__slug=product_slug, warehouse__id=warehouse_id)
        warehouse_product_serializer = WarehouseProductSerializer(warehouse_product_object)
        return Response(warehouse_product_serializer.data, status=200)


class NewWarehouseProducts(APIView):

    def get(self, request):
        warehouse_id = request.GET['warehouse_id']
        new_warehouse_product_objects = WarehouseProduct.objects.filter(warehouse__id=warehouse_id).order_by('-modified_date')[:25]
        new_warehouse_product_serializer = WarehouseProductSerializer(new_warehouse_product_objects, many=True)
        return Response(new_warehouse_product_serializer.data, status=200)
