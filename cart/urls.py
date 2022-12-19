from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartProductsListView.as_view(), name='cart_products'),
    path('delete/<int:cart_item_id>', views.DeleteCartProduct.as_view(), name='delete_cart_item'),
    path('add', views.AddCartProduct.as_view(), name='add_cart_item'),
    path('increase-quantity', views.IncreaseCartProductQuantity.as_view(), name='increase_cart_item_quantity'),
    path('decrease-quantity', views.DecreaseCartProductQuantity.as_view(), name='decrease_cart_item_quantity'),
    path('empty-cart', views.EmptyCart.as_view(), name='empty_cart'),

]
