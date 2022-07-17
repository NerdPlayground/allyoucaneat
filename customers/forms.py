from customers.models import Customers
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomerRegistration(UserCreationForm):
    class Meta:
        model= Customers
        fields= [
            "first_name","last_name",
            "phone_number","password1","password2"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'id':'first_name', 
                'placeholder': 'Enter first name'
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'id':'last_name', 
                'placeholder': 'Enter last name'
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'id':'phone_number', 
                'placeholder': 'Enter phone number',
                "maxlength":"13",
                "minlength":"13",
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'id':'password1', 
                'placeholder': 'Enter password'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'id':'password2', 
                'placeholder': 'Re-type password'
            }
        )

class ModificationForm(UserChangeForm):
    class Meta:
        model= Customers
        fields= [
            "first_name","last_name",
            "email","phone_number"
        ]