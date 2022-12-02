from django.shortcuts import render
from rest_framework.views import APIView
from accounts.models import Account
from .models import CartProduct
from .serializers import CartProductSerializer
from rest_framework.response import Response


class CartProductsListView(APIView):
    def get(self, request):
        try:
            user_id = request.GET['user_id']
            user_object = Account.objects.get(id=user_id)
            cart_product_objects = CartProduct.objects.filter(user=user_object)
            cart_products_serializer = CartProductSerializer(cart_product_objects, many=True)
            return Response(cart_products_serializer.data, status=200)
        except Exception as e:
            print(e)
            return Response(status=500)
