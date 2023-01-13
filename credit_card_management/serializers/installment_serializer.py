from rest_framework import serializers
from credit_card_management.models import Installment


class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = ['id', 'purchase', 'number', 'value_paid', 'date', 'paid']
