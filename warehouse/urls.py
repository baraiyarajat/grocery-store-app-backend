from django.urls import path
from . import views

urlpatterns = [
    path('', views.warehouse_list, name='warehouse_list'),
    path('<int:warehouse_id>', views.warehouse_details, name='warehouse_details'),
    path('selected-warehouse', views.SelectedWarehouseViewAPI.as_view(), name='selected_warehouse'),
]
