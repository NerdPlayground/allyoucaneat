from django import forms

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