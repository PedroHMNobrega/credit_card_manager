from rest_framework import serializers
from credit_card_management.models import Category
import credit_card_management.validators as validators


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate(self, data):
        if not validators.valid_name(data['name']):
            raise serializers.ValidationError({'name': "Invalid name"})

        return data
