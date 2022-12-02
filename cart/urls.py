from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartProductsListView.as_view(), name='cart_products'),

]
