from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrdersListView.as_view(), name='orders_list'),
    path('<int:order_id>', views.OrderDetailView.as_view(), name='order_details'),
    path('place-order', views.PlaceOrderView.as_view(), name='place_order')
]
