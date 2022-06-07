from django import forms
from custom_user.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    status= forms.ChoiceField(
        label="Status",
        choices=(
            ("Customer","Customer"),
            ("SasaPay Vendor","SasaPay Vendor"),
            ("External Vendor","External Vendor"),
        )
    )
    class Meta:
        model= User
        fields= [
            "status","first_name","last_name",
            "phone_number","email","password1","password2"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update(
            {
                'id': 'status',
                'autofocus': 'autofocus'
            }
        )
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
        self.fields['email'].widget.attrs.update(
            {
                'id':'email', 
                'placeholder': 'Enter email'
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
    email= forms.EmailField(label="Email")
    password= forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    
    email.widget.attrs.update(
        {
            'id':'email',
            'autofocus': 'autofocus',
            'placeholder': 'Enter email'
        }
    )
    password.widget.attrs.update(
        {
            'id':'password',
            'placeholder': 'Enter password'
        }
    )