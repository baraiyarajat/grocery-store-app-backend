from django.urls import path
from . import views

urlpatterns = [
    path('', views.WarehouseProductListView.as_view(), name='warehouse_product_list'),
    path('newly-added-products', views.NewWarehouseProducts.as_view(), name='new_warehouse_product_list'),
    path('featured-products', views.FeaturedProducts.as_view(), name='featured_product_list'),
    path('search-products', views.SearchProducts.as_view(), name='search_product_list'),
    path('<slug:product_slug>', views.WarehouseProductDetailsView.as_view(), name='warehouse_product_details'),
]
