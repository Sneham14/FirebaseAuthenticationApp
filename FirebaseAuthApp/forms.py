from django import forms
from django.core.exceptions import ValidationError

class UserForm(forms.Form):
    user_name=forms.CharField(max_length=120)
    user_email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        error_messages={
            'required': 'Please enter your email.',
            'invalid': 'Please enter a valid email address.',
            'max_length': 'Email address is too long.',
        })
    user_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        error_messages={
            'required': 'Please enter your password.',
        })
    
    def password_validation(self):
        user_password = self.cleaned_data.get('user_password')
        if len(user_password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return user_password
    

