from rest_framework import viewsets
from credit_card_management.serializers import InstallmentSerializer
from credit_card_management.models import Installment


class InstallmentViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentSerializer
    http_method_names = ['get', 'put']

    def get_queryset(self):
        user = self.request.user
        queryset = Installment.objects.filter(user_id=user.id)
        return queryset
