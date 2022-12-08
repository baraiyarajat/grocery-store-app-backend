from django.db import models
from accounts.models import Account


class Wallet(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    credit = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    cashback_balance = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    modified_date = models.DateTimeField(auto_now=True)

    def formatted_modified_date(self):
        return self.modified_date.strftime("%b %d %Y")
