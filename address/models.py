from django.db import models
from accounts.models import Account
from warehouse.models import Warehouse


class Address(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=50, default='home', unique=False)
    address_line_1 = models.CharField(max_length=300, null=False, blank=False)
    address_line_2 = models.CharField(max_length=300, null=False, blank=False)
    pincode = models.CharField(max_length=8, blank=False, null=False)
    city = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    class META:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
