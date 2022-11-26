from django.urls import path
from . import views

urlpatterns = [
    path('', views.WarehouseProductListView.as_view(), name='warehouse_product_list'),
]
