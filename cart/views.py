from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import Account
from .models import CartProduct
from .serializers import CartProductSerializer
from rest_framework.response import Response
from warehouse.models import Warehouse
from warehouse_product.models import WarehouseProduct


class CartProductsListView(APIView):
    def get(self, request):
        try:
            user_id = request.GET['user_id']
            selected_warehouse_id = request.GET['selected_warehouse_id']
            user_object = Account.objects.get(id=user_id)
            warehouse_object = Warehouse.objects.get(id=selected_warehouse_id)
            cart_product_objects = CartProduct.objects.filter(user=user_object,
                                                              warehouse=warehouse_object)
            cart_products_serializer = CartProductSerializer(cart_product_objects, many=True)
            return Response(cart_products_serializer.data, status=200)
        except Exception as e:
            print(e)
            return Response(status=500)


class DeleteCartProduct(APIView):
    def delete(self, request, cart_item_id):
        try:
            cart_item_object = CartProduct.objects.get(id=cart_item_id)
            cart_item_object.delete()
            return Response(status=200)
        except Exception as e:
            print(e)
            return Response(status=500)


class IncreaseCartProductQuantity(APIView):

    def patch(self, request):

        try:
            cart_product_id = request.data['cart_product_id']
            cart_product_object = CartProduct.objects.get(id=cart_product_id)
            cart_product_object.quantity += 1
            cart_product_object.save()
            return Response(status=200)
        except Exception as e:
            return Response(status=500)


class DecreaseCartProductQuantity(APIView):

    def patch(self, request):

        try:
            cart_product_id = request.data['cart_product_id']
            cart_product_object = CartProduct.objects.get(id=cart_product_id)
            cart_product_object.quantity -= 1

            if cart_product_object.quantity == 0:
                cart_product_object.delete()
            else:
                cart_product_object.save()
            return Response(status=200)
        except Exception as e:
            return Response(status=500)


class AddCartProduct(APIView):
    def post(self, request):

        try:
            print(request.data)
            user_id = request.data['user_id']
            warehouse_id = request.data['warehouse_id']
            warehouse_product_id = request.data['warehouse_product_id']

            user_object = Account.objects.get(id=user_id)
            warehouse_object = Warehouse.objects.get(id=warehouse_id)
            warehouse_product_object = WarehouseProduct.objects.get(id=warehouse_product_id)

            CartProduct.objects.create(user=user_object,
                                       warehouse=warehouse_object,
                                       warehouse_product=warehouse_product_object).save()

            return Response(status=200)
        except Exception as e:
            print(e)
            return Response(status=500)
