from django.db import models
from accounts.models import Account


class Warehouse(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    default_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SelectedWarehouse(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.warehouse.name
