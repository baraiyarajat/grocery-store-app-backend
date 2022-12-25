from django.db import models
from accounts.models import Account
from warehouse_product.models import WarehouseProduct
from warehouse.models import Warehouse

ORDER_STATUS_VALUES = (
    ("PLACED", "Placed"),
    ("FAILED", "Failed"),
    ("PENDING", "Pending"),
    ("REJECTED", "Rejected"),
    ("DELIVERED", "Delivered"),
    ("ON_THE_WAY", "On the way"),
    ("PACKED", "Packed"),
    ("CANCELLED", "Cancelled")
)

PAYMENT_METHOD_VALUES = (
    ("COD", "COD"),
    ("CARD", "CARD"),
    ("WALLET", "WALLET"),
)

DELIVERY_TIME_VALUES = (
    ("8", "8:00 AM to 10:00 AM"),
    ("10", "10:00 AM to 12:00 PM"),
    ("12", "12:00 PM to 14:00 PM"),
    ("14", "14:00 PM to 16:00 PM"),
    ("16", "16:00 PM to 18:00 PM"),
)


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=128, default="")
    status = models.CharField(
        max_length=64,
        choices=ORDER_STATUS_VALUES,
        default='PENDING'
    )
    payment_method = models.CharField(max_length=64, default="COD", choices=PAYMENT_METHOD_VALUES)
    card_number = models.CharField(null=True, max_length=16, default="", blank=True)
    savings = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    delivery_fee = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    cart_amount = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    final_amount = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    payment_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    total_items = models.IntegerField(default=0)
    delivery_date = models.CharField(max_length=64, default="")
    delivery_time = models.CharField(max_length=64, choices=DELIVERY_TIME_VALUES, default="8")

    def formatted_order_status(self):
        return dict(ORDER_STATUS_VALUES)[self.status]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    warehouse_item = models.ForeignKey(WarehouseProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
