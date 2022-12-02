from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartProductsListView.as_view(), name='cart_products'),
    path('delete/<int:cart_item_id>', views.DeleteCartProduct.as_view(),name='delete_cart_item')

]
