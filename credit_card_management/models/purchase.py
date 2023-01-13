from django.db import models
from django.contrib.auth.models import User
from datetime import date
from credit_card_management.models import Category


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    installmentsNumber = models.IntegerField(blank=False, null=False)
    value = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    firstInstallmentDate = models.DateField(default=date.today, blank=True)

    def __str__(self):
        return self.name