from django.shortcuts import render
from rest_framework.views import APIView
from .models import Address
from .serializers import AddressSerializer
from rest_framework.response import Response


class AddressListView(APIView):

    def get(self, request):
        user_id = request.GET['user_id']
        addresses = Address.objects.filter(user__id=user_id)
        address_serializer = AddressSerializer(addresses, many=True)
        return Response(address_serializer.data, status=200)
