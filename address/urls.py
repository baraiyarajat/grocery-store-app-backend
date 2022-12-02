from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddressListView.as_view(), name='address_list'),
    path('add-address', views.AddAddressView.as_view(), name='add_address'),
    path('edit-address', views.EditAddressView.as_view(),name='edit_address'),
    path('<int:address_id>', views.AddressDetailView.as_view(), name='address_detail')
]
