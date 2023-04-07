from rest_framework import serializers
from credit_card_management.models import Purchase
from credit_card_management.serializers import CategorySerializer


class PurchaseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'name', 'installmentsNumber', 'value', 'category', 'firstInstallmentDate']