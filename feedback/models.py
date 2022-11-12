import uuid
from django.db import models

class Feedback(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    customer=models.ForeignKey(
        "customers.Customers",
        related_name="feedback",
        on_delete=models.CASCADE
    )
    vendor= models.ForeignKey(
        "vendors.Vendor",
        related_name="feedback",
        on_delete=models.CASCADE
    )
    receipt=models.ForeignKey(
        "receipts.Receipt",
        related_name="feedback",
        on_delete=models.DO_NOTHING
    )
    content=models.TextField()
    shop= models.CharField(max_length=255)
    created_on=models.DateTimeField(auto_now_add=True)