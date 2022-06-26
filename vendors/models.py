from django.db import models
from custom_user.models import User

class Vendor(User):
    business_name= models.CharField(max_length=255,blank=False)
    till_number= models.CharField(max_length=255,unique=True,blank=False)