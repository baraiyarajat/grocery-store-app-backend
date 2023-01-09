from django.shortcuts import render
from rest_framework.views import APIView
from .models import Address
from .serializers import AddressSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Account
from warehouse.models import Warehouse


class AddressListView(APIView):

    def get(self, request):
        user_id = request.GET['user_id']
        addresses = Address.objects.filter(user__id=user_id)
        address_serializer = AddressSerializer(addresses, many=True)
        return Response(address_serializer.data, status=200)


class AddressDetailView(APIView):

    def delete(self, request, address_id):
        try:
            address_object = Address.objects.get(id=address_id)
            address_object.delete()

            response = Response()
            response.status = 200
            response.data = {
                'success_message': 'Address deleted successfully'
            }

            return response
        except ObjectDoesNotExist:

            response = Response()
            response.status = 500
            response.data = {
                'error_message': 'Either the address is deleted or it does not exist.'
            }
            return response

        except Exception as e:

            response = Response()
            response.status = 500
            response.data = {
                'error_message': 'Some error occurred while deleting the address'
            }
            return response


class AddAddressView(APIView):

    def post(self, request):

        try:
            user_id = request.data['user_id']
            address_type = request.data['address_type']
            address_line_1 = request.data['address_line_1']
            address_line_2 = request.data['address_line_2']
            pincode = request.data['pincode']
            city = request.data['city']

            user_object = Account.objects.get(id=user_id)
            warehouse_object = Warehouse.objects.get(name=city)

            Address.objects.create(user=user_object,
                                   address_type=address_type,
                                   address_line_1=address_line_1,
                                   address_line_2=address_line_2,
                                   pincode=pincode,
                                   city=warehouse_object).save()

            response = Response()
            response.status = 200
            response.data = {
                'success_message': 'Address added successfully.'
            }

            return response
        except Exception as e:
            print(e)

            response = Response()
            response.status = 500
            response.data = {
                'error_message': 'Some error occurred while adding the address'
            }

            return response


class EditAddressView(APIView):

    def patch(self, request):

        try:
            address_id = request.data['address_id']
            user_id = request.data['user_id']
            address_type = request.data['address_type']
            address_line_1 = request.data['address_line_1']
            address_line_2 = request.data['address_line_2']
            pincode = request.data['pincode']
            city = request.data['city']

            user_object = Account.objects.get(id=user_id)
            warehouse_object = Warehouse.objects.get(name=city)

            address_object = Address.objects.get(id=address_id, user=user_object)

            address_object.address_line_1 = address_line_1
            address_object.address_line_2 = address_line_2
            address_object.pincode = pincode
            address_object.city = warehouse_object
            address_object.address_type = address_type
            address_object.save()

            response = Response()
            response.status = 200
            response.data = {
                'success_message': 'Address edited successfully.'
            }

            return response
        except Exception as e:
            print(e)
            response = Response()
            response.status = 500
            response.data = {
                'error_message': 'Some error occurred while editing the address'
            }

            return response
