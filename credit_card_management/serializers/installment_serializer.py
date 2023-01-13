from rest_framework import serializers
from credit_card_management.models import Installment


class InstallmentSerializer(serializers.ModelSerializer):
    purchase_name = serializers.ReadOnlyField(source='purchase.name')

    class Meta:
        model = Installment
        fields = ['id', 'purchase_name', 'number', 'value_paid', 'date', 'paid']
