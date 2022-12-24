from .models import Warehouse, SelectedWarehouse
from accounts.models import Account
from rest_framework.decorators import api_view
from .serializers import WarehouseSerializer, SelectedWarehouseSerializer
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(['GET', ])
def warehouse_list(request):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()

        warehouse_serializer = WarehouseSerializer(warehouses, many=True)
        return JsonResponse(warehouse_serializer.data, safe=False)


@api_view(['GET', ])
def warehouse_details(request, warehouse_id):
    if request.method == 'GET':
        warehouse = Warehouse.objects.get(id=warehouse_id)
        warehouse_serializer = WarehouseSerializer(warehouse)
        return JsonResponse(warehouse_serializer.data, safe=False)


class SelectedWarehouseViewAPI(APIView):

    def post(self, request):

        user_id = request.data['user_id']
        if not user_id:
            selected_warehouse_object = Warehouse.objects.get(default_selected=True)
            response = Response()
            response.data = {'warehouse': WarehouseSerializer(selected_warehouse_object).data}
            response.status=200
            return response
        user = Account.objects.get(id=user_id)
        selected_warehouse_id = request.data['selected_warehouse_id']

        if selected_warehouse_id is None:
            try:
                selected_warehouse_object = SelectedWarehouse.objects.get(user=user)
            except ObjectDoesNotExist as e:
                warehouse_object = Warehouse.objects.get(default_selected=True)
                selected_warehouse_object = SelectedWarehouse.objects.create(user=user, warehouse=warehouse_object)

        else:
            selected_warehouse_object = SelectedWarehouse.objects.get(user=user)
            warehouse_object = Warehouse.objects.get(id=selected_warehouse_id)
            selected_warehouse_object.warehouse = warehouse_object
            selected_warehouse_object.save()

        return Response(SelectedWarehouseSerializer(selected_warehouse_object).data, status=200)
