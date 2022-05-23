import uuid
from django.db import models

class Product(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name= models.CharField(max_length=255)

class Content(models.Model):
    name= models.CharField(max_length=255)
    product= models.ForeignKey(
        "products.Product",
        related_name="contents",
        on_delete=models.CASCADE
    )

class Price(models.Model):
    value= models.IntegerField()
    type= models.CharField(max_length=255)
    product= models.ForeignKey(
        "products.Product",
        related_name="prices",
        on_delete=models.CASCADE
    )