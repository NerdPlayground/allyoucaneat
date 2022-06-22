# Generated by Django 4.0.4 on 2022-06-22 07:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentProcessResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('MerchantRequestID', models.CharField(max_length=255)),
                ('CheckoutRequestID', models.CharField(max_length=255)),
                ('ResultCode', models.IntegerField()),
                ('ResultDesc', models.CharField(max_length=255)),
                ('TransAmount', models.CharField(max_length=255)),
                ('BillRefNumber', models.CharField(max_length=255)),
                ('TransactionDate', models.CharField(max_length=255)),
                ('CustomerMobile', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RequestPaymentResponse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('detail', models.CharField(max_length=255)),
                ('PaymentGateway', models.CharField(max_length=255)),
                ('MerchantRequestID', models.CharField(max_length=255)),
                ('CheckoutRequestID', models.CharField(max_length=255)),
                ('ResponseCode', models.CharField(max_length=255)),
                ('ResponseDescription', models.CharField(max_length=255)),
                ('CustomerMessage', models.CharField(max_length=255)),
            ],
        ),
    ]
