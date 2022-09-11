from vendors.models import Vendor
from custom_user.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

class VendorRegistration(UserCreationForm):
    class Meta:
        model= Vendor
        fields= [
            "first_name","last_name","phone_number",
            "business_name","till_number",
            "password1","password2"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {
                "id":"first_name",
                "autofocus": "autofocus",
                "placeholder": "Enter first name"
            }
        )
        self.fields["last_name"].widget.attrs.update(
            {
                "id":"last_name", 
                "placeholder": "Enter last name"
            }
        )
        self.fields["phone_number"].widget.attrs.update(
            {
                "id":"phone_number", 
                "placeholder": "Enter phone number",
                "maxlength":"13",
                "minlength":"13",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "id":"password1", 
                "placeholder": "Enter password"
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "id":"password2", 
                "placeholder": "Re-type password"
            }
        )
        self.fields["business_name"].widget.attrs.update(
            {
                "id":"business_name",
                "placeholder":"Enter business name"
            }
        )
        self.fields["till_number"].widget.attrs.update(
            {
                "id":"till_number",
                "placeholder":"Enter business number"
            }
        )

class ModificationForm(UserChangeForm):
    class Meta:
        model= Vendor
        fields= [
            "first_name","last_name",
            "email","phone_number",
            "business_name","till_number"
        ]