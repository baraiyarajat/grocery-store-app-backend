"""grocery_store_app_backend URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls')),
                  path('api/v0/warehouses/', include('warehouse.urls')),
                  path('api/v0/addresses/', include('address.urls')),
                  path('api/v0/categories/', include('category.urls')),
                  path('api/v0/warehouse_products/', include('warehouse_product.urls')),
                  path('api/v0/wishlist/', include('wishlist.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
