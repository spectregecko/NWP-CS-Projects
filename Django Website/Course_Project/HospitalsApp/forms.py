from django import forms
from .models import Hospital, MyEmail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class NewHospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'zip_code', 'phone', 'type', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Example Hospital'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Canadian or American'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'234-567-8901'}),
            'type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Public/Private/Nonprofit'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'someone@example.ca'}),
        }

class SendEmailForm(forms.ModelForm):

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Enter your Email Password'})
    )

    class Meta:
        model = MyEmail
        fields = ['password', 'receiver', 'subject', 'message']

        widgets = {
            'receiver': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Receiver\'s Email'}),
            'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the Subject'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter a Message'}),
        }

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'fbob'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fred'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bob'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'someone@example.ca'}),
        }