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
                                                                    warehouse__id=warehouse_id).order_by(
            'product__name')
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

        if 'category_slug' in request.GET.keys():
            category_slug = request.GET['category_slug']
            category_object = Category.objects.get(slug=category_slug)
            new_warehouse_product_objects = WarehouseProduct.objects.filter(
                warehouse__id=warehouse_id, product__category=category_object).order_by('-modified_date')[:25]
            new_warehouse_product_serializer = WarehouseProductSerializer(new_warehouse_product_objects, many=True)
        else:

            new_warehouse_product_objects = WarehouseProduct.objects.filter(
                warehouse__id=warehouse_id).order_by('-modified_date')[:25]
            new_warehouse_product_serializer = WarehouseProductSerializer(new_warehouse_product_objects, many=True)
        return Response(new_warehouse_product_serializer.data, status=200)


class FeaturedProducts(APIView):

    def get(self, request):
        warehouse_id = request.GET['warehouse_id']
        featured_product_objects = WarehouseProduct.objects.filter(warehouse__id=warehouse_id,
                                                                   is_featured=True)

        featured_product_serializer = WarehouseProductSerializer(featured_product_objects, many=True)

        return Response(featured_product_serializer.data, status=200)


class SearchProducts(APIView):

    def get(self, request):

        try:
            warehouse_id = request.GET['warehouse_id']
            search_string = request.GET['search_string']

            search_result_objects = WarehouseProduct.objects.filter(warehouse__id=warehouse_id, product__name__icontains= search_string)
            search_product_serializer = WarehouseProductSerializer(search_result_objects, many=True)
            return Response(search_product_serializer.data, status=200)

        except Exception as e:
            print(e)
            return Response(status=500)

