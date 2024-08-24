from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Username'
                    }
                ),

            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Email Addres'
                    }
                ),
            
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'type': 'password',
                    'placeholder':'Password'
                    }
                ),
            
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Confirm Password'
                }
            ),
            
        }