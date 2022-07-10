from django import forms
from custom_user.forms import RegistrationForm

class VendorRegistration(RegistrationForm):
    business_name= forms.CharField(label="Business Name",max_length=255)
    business_number= forms.CharField(label="Business Number",max_length=255)
    
    business_name.widget.attrs.update(
        {
            "id":"business_name",
            "placeholder":"Enter business name"
        }
    )
    business_number.widget.attrs.update(
        {
            "id":"business_number",
            "placeholder":"Enter business number"
        }
    )