import uuid
from django.db import models

class RequestPaymentResponse(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    status= models.BooleanField()
    detail= models.CharField(max_length=255)
    PaymentGateway= models.CharField(max_length=255)
    MerchantRequestID= models.CharField(max_length=255)
    CheckoutRequestID= models.CharField(max_length=255)
    ResponseCode= models.CharField(max_length=255)
    ResponseDescription= models.CharField(max_length=255)
    CustomerMessage= models.CharField(max_length=255)

class PaymentProcessResult(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    MerchantRequestID= models.CharField(max_length=255)
    CheckoutRequestID= models.CharField(max_length=255)
    ResultCode= models.IntegerField()
    ResultDesc= models.CharField(max_length=255)
    TransAmount= models.CharField(max_length=255)
    BillRefNumber= models.CharField(max_length=255)
    TransactionDate= models.CharField(max_length=255)
    CustomerMobile= models.CharField(max_length=255)