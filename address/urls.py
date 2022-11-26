from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddressListView.as_view(), name='address_list'),
    path('<int:address_id>', views.AddressDetailView.as_view(), name='address_detail')
]
