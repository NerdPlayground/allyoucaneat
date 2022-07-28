import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Receipt(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    product_name= models.CharField(max_length=255)
    contents= ArrayField(models.CharField(max_length=255))
    product_type= models.CharField(max_length=255)
    price= models.IntegerField()
    customer= models.ForeignKey(
        "customers.Customers",
        related_name="receipts",
        on_delete= models.DO_NOTHING
    )
    vendor= models.ForeignKey(
        "vendors.Vendor",
        related_name="receipts",
        on_delete= models.DO_NOTHING
    )
    shop= models.CharField(max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s receipt" %(self.customer.get_full_name(),self.product_name)