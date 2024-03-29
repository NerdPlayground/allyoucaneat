import uuid
from django.db import models

class Order(models.Model):
    id= models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    product= models.ForeignKey(
        "products.Product",
        related_name="orders",
        on_delete= models.DO_NOTHING
    )
    contents= models.ManyToManyField(
        "products.Content",
        related_name="orders",
    )
    price= models.ForeignKey(
        "products.Price",
        related_name="price",
        on_delete= models.DO_NOTHING
    )
    customer= models.ForeignKey(
        "custom_user.User",
        related_name="orders",
        on_delete= models.DO_NOTHING
    )
    extra_instructions= models.TextField(null=True,blank=True)
    paid= models.BooleanField(default=False)
    delivered= models.BooleanField(default=False)
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s's order" %(self.customer.first_name)