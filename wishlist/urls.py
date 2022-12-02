from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishListView.as_view(), name='wishlist'),
    path('<int:wishlist_product_id>', views.WishlistProductDetailView.as_view(), name='wishlist_product_detail'),
    path('add-product-to-wishlist/', views.WishlistProductDetailView.as_view(), name='add_product_to_wishlist')
]
