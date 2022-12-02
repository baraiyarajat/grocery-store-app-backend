from django.shortcuts import render
from rest_framework.views import APIView
from .models import WishlistProduct
from rest_framework.response import Response
from warehouse.models import Warehouse
from .serializers import WishlistSerializer
from django.core.exceptions import ObjectDoesNotExist
from warehouse_product.models import WarehouseProduct
from accounts.models import Account


class WishListView(APIView):

    def get(self, request):

        user_id = request.GET['user_id']
        warehouse_id = request.GET['warehouse_id']
        warehouse_object = Warehouse.objects.get(id=warehouse_id)
        wishlist_products = WishlistProduct.objects.filter(user__id=user_id,
                                                           warehouse_product__warehouse=warehouse_object)
        wishlist_serializer = WishlistSerializer(wishlist_products, many=True)

        return Response(wishlist_serializer.data, status=200)


class WishlistProductDetailView(APIView):

    def delete(self, request, wishlist_product_id):
        try:
            wishlist_product_object = WishlistProduct.objects.get(id=wishlist_product_id)
            wishlist_product_object.delete()
            return Response(data={'wishlist_product_id':wishlist_product_id}, status=200)
        except ObjectDoesNotExist:
            return Response(status=204)

    def put(self, request):

        # print(request.data)

        user_id = request.data['user_id']
        warehouse_product_id = request.data['warehouse_product_id']
        warehouse_product_object = WarehouseProduct.objects.get(id=warehouse_product_id)
        user_object = Account.objects.get(id=user_id)
        if not WishlistProduct.objects.filter(user=user_object, warehouse_product=warehouse_product_object).exists():

            try:
                wishlist_product_object = WishlistProduct.objects.create(user=user_object,
                                                                         warehouse_product=warehouse_product_object)
                wishlist_serializer = WishlistSerializer(wishlist_product_object)
                return Response(wishlist_serializer.data, status=200)
            except Exception as e:
                print(e)
                return Response( status=500)
        else:
            return Response(status=200)