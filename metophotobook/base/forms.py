from django import forms
from .models import *


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'photo_avatar', 'email', 'password']