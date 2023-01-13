from rest_framework import viewsets, status
from credit_card_management.serializers import PurchaseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from credit_card_management.models import Purchase, Category
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    http_method_names = ['get', 'put', 'post', 'delete']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def create(self, request, *args, **kwargs):
        if not self.valid_category():
            raise ValidationError({'category': "Category does not exist"})

        user = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        return response

    def perform_update(self, serializer):
        if self.valid_category():
            serializer.save()
        else:
            raise ValidationError({'category': "Category does not exist"})

    def get_queryset(self):
        user = self.request.user
        queryset = Purchase.objects.filter(user_id=user.id)
        return queryset

    def valid_category(self):
        if 'category' not in self.request.data.keys():
            return True

        user = self.request.user
        category = Category.objects.filter(pk=self.request.data['category'], user=user.id)
        return len(category) == 1