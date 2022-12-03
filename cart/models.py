from django.db import models
from accounts.models import Account
from warehouse_product.models import WarehouseProduct
from warehouse.models import Warehouse


class CartProduct(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    warehouse_product = models.ForeignKey(WarehouseProduct, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'warehouse_product'),)

    def __str__(self):
        return self.warehouse_product.product.name
