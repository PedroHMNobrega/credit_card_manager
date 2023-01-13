from rest_framework import viewsets, status
from credit_card_management.serializers import PurchaseSerializer
from credit_card_management.models import Purchase, Category
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        self.validate_category()

        user = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        return response

    def get_queryset(self):
        user = self.request.user
        queryset = Purchase.objects.filter(user_id=user.id)
        return queryset

    def validate_category(self):
        if 'category' not in self.request.data.keys():
            return True

        user = self.request.user
        category = Category.objects.filter(pk=self.request.data['category'], user=user.id)
        if len(category) != 1:
            raise ValidationError({'category': "Category does not exist"})
