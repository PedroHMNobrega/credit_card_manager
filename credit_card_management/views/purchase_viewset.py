from django.db import transaction
from rest_framework import viewsets, status
from credit_card_management.serializers import PurchaseSerializer, InstallmentSerializer
from credit_card_management.models import Purchase, Category
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    http_method_names = ['get', 'post', 'delete']

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            self.validate_category()

            user = request.user
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            purchase = serializer.save(user=user)
            self.create_installments(purchase)

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

    def create_installments(self, purchase):
        user = self.request.user
        first_installment_value = purchase.get_first_installment_value
        other_installment_value = purchase.get_installment_value
        installment_date = purchase.firstInstallmentDate

        for installment_number in range(1, purchase.installmentsNumber + 1):
            installment_value = other_installment_value
            if installment_number == 1:
                installment_value = first_installment_value

            installment = {
                'purchase': purchase.id,
                'number': installment_number,
                'value_paid': installment_value,
                'date': installment_date
            }

            installment_serializer = InstallmentSerializer(data=installment)
            installment_serializer.is_valid(raise_exception=True)
            installment_serializer.save(user=user)

            installment_date += relativedelta(months=1)
