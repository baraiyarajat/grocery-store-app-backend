from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<int:category_id>', views.category_details, name='category_details'),
    path('<slug:category_slug>', views.category_details_by_slug, name='category_details_by_slug'),
]
