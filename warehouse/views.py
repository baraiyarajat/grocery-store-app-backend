from .models import Warehouse
from rest_framework.decorators import api_view
from .serializers import WarehouseSerializer
from django.http.response import JsonResponse


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
