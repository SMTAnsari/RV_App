from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms

class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(label='Phone Number', max_length=10, widget=forms.TextInput(attrs={'type': 'tel', 'pattern': '[0-9]{10}', 'title': 'Please enter a 10-digit phone number','value': '+91'}))
    class Meta:
        model = User
        fields = ['username', 'email','phone_number', 'password1', 'password2']
    
