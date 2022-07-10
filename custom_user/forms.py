from django import forms
from custom_user.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
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
                'placeholder': 'Enter phone number'
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

class AuthenticationForm(forms.Form):
    phone_number= forms.CharField(label="Phone Number")
    password= forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    
    phone_number.widget.attrs.update(
        {
            'id':'phone_number',
            'autofocus': 'autofocus',
            'placeholder': 'Enter phone number'
        }
    )
    password.widget.attrs.update(
        {
            'id':'password',
            'placeholder': 'Enter password'
        }
    )