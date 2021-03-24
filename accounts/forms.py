from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Select Username',
                }),
            'email': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'user@user.com',
                }),
            'password1': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password1',
                }),
            'password2': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password2',
                }),
        }