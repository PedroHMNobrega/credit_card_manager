from rest_framework import serializers
from credit_card_management.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'name', 'installmentsNumber', 'value', 'category', 'firstInstallmentDate']