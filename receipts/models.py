import uuid
from django.db import models

class Receipt(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    order= models.OneToOneField(
        "orders.Order",
        related_name="receipt",
        on_delete= models.DO_NOTHING
    )
    customer= models.ForeignKey(
        "custom_user.User",
        related_name="customer_receipts",
        on_delete= models.DO_NOTHING
    )
    vendor= models.ForeignKey(
        "custom_user.User",
        related_name="vendor_receipts",
        on_delete= models.DO_NOTHING
    )
    paid= models.BooleanField(default=False)
    ready= models.BooleanField(default=False)
    created_on= models.DateTimeField(auto_now_add=True)