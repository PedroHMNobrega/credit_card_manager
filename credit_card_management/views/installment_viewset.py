from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from credit_card_management.serializers import InstallmentSerializer
from credit_card_management.models import Installment


class InstallmentViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentSerializer
    http_method_names = ['get', 'put']

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
