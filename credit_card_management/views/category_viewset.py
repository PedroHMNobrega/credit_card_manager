from rest_framework import viewsets
from credit_card_management.serializers import CategorySerializer
from credit_card_management.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'delete']
