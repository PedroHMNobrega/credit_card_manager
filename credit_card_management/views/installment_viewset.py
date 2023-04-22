import decimal

from django.db.transaction import atomic
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

        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        queryset = Installment.objects.filter(user_id=user.id)

        if month and year:
            queryset = queryset.filter(date__month=month, date__year=year)

        return queryset

    @atomic
    def update(self, request, *args, **kwargs):
        try:
            user = request.user
            installment_id = kwargs['pk']

            installment = Installment.objects.get(pk=installment_id, user=user.id)

            if installment.paid == request.data['paid']:
                raise KeyError

            installment.paid = request.data['paid']

            if installment.paid:
                installment.value_paid = request.data['value_paid']

            installment.save()

            self.update_purchase(installment)

            serializer = InstallmentSerializer(installment)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyError:
            raise ValidationError({'detail': 'Invalid input.'})
        except:
            raise NotFound()

    def update_purchase(self, installment):
        paid = installment.paid
        value_paid = decimal.Decimal(installment.value_paid)
        purchase = installment.purchase

        if paid:
            purchase.installments_paid += 1
            purchase.value_paid += value_paid
        else:
            purchase.installments_paid -= 1
            purchase.value_paid -= value_paid

        purchase.save()
