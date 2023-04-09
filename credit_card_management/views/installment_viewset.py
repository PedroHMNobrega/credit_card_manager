from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from credit_card_management.serializers import InstallmentSerializer, ListInstallmentSerializer
from credit_card_management.models import Installment


class InstallmentViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListInstallmentSerializer
        else:
            return InstallmentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Installment.objects.filter(user_id=user.id)
        return queryset

    def update(self, request, *args, **kwargs):
        try:
            user = request.user
            installment_id = kwargs['pk']

            installment = Installment.objects.get(pk=installment_id, user=user.id)

            installment.paid = request.data['paid']
            installment.value_paid = request.data['value_paid']

            installment.save()

            serializer = InstallmentSerializer(installment)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            raise ValidationError({'detail': 'Invalid input.'})
        except:
            raise NotFound()
