from django.db import models
from accounts.models import Account
from warehouse_product.models import WarehouseProduct


class WishlistProduct(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    warehouse_product = models.ForeignKey(WarehouseProduct, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'warehouse_product'),)

    def __str__(self):
        return self.warehouse_product.product.name