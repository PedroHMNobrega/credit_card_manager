# Generated by Django 4.1.5 on 2023-04-18 13:47

from django.db import migrations, models
from django.db.models import Sum


def populate_field(apps, schema_editor):
    Installment = apps.get_model("credit_card_management", "Installment")
    Purchase = apps.get_model("credit_card_management", "Purchase")

    for purchase in Purchase.objects.all():
        installments_paid = Installment.objects.filter(
            purchase=purchase.pk,
            paid=True
        )
        purchase.installments_paid = installments_paid.count()
        purchase.value_paid = installments_paid.aggregate(Sum('value_paid'))['value_paid__sum'] or 0
        purchase.save(update_fields=["installments_paid", "value_paid"])


class Migration(migrations.Migration):
    dependencies = [
        ("credit_card_management", "0005_installment"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="installments_paid",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="purchase",
            name="value_paid",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.RunPython(
            code=populate_field,
            reverse_code=migrations.RunPython.noop
        ),
    ]
