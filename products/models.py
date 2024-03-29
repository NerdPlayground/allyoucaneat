import uuid
from django.db import models

class Product(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name= models.CharField(max_length=255)
    vendor= models.ForeignKey(
        "vendors.Vendor",
        related_name="products",
        on_delete= models.CASCADE
    )

    def __str__(self):
        return self.name

class Content(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name= models.CharField(max_length=255)
    product= models.ForeignKey(
        "products.Product",
        related_name="contents",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s content" %(self.product)

class Price(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    value= models.IntegerField()
    type= models.CharField(max_length=255)
    product= models.ForeignKey(
        "products.Product",
        related_name="prices",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s price" %(str(self.product))