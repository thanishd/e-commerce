from django.contrib.auth.forms import UserCreationForm 
from django import forms
from app.models import User

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm_Password'}))
    class Meta:
        model=User
        fields=[
            'username','email','password1','password2'
        ]