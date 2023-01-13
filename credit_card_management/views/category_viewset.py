from rest_framework import viewsets, status
from rest_framework.response import Response

from credit_card_management.serializers import CategorySerializer
from credit_card_management.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        return response

    def get_queryset(self):
        user = self.request.user
        queryset = Category.objects.filter(user_id=user.id)
        return queryset