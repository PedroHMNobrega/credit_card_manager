from django.contrib.auth.models import User
from django.db import models
from datetime import date
from credit_card_management.models import Purchase


class Installment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=False, null=False)
    number = models.IntegerField(default=1, null=True, blank=True)
    value_paid = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    date = models.DateField(default=date.today, blank=True)
    paid = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'${self.purchase.name} - ${self.number}/${self.purchase.installmentsNumber}'
