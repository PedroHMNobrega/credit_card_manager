from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ['email']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['name'] = f"{instance.first_name} {instance.last_name}"
        return representation