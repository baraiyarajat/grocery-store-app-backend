from django.db import models
from warehouse.models import Warehouse
from product.models import Product


class WarehouseProduct(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    discount_rate = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = (('warehouse', 'product'),)

    def __str__(self):
        return "{}/{}".format(self.warehouse.name,self.product.name)

    def get_discounted_price(self):
        return round(self.price - (self.price * self.discount_rate / 100), 2)
