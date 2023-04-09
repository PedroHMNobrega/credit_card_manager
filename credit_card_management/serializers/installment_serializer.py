from rest_framework import serializers
from credit_card_management.models import Installment
from credit_card_management.serializers import PurchaseSerializer


class InstallmentSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer()
    category = serializers.CharField(source='purchase.category')

    class Meta:
        model = Installment
        fields = ['id', 'purchase', 'number', 'value_paid', 'date', 'paid', 'category']
