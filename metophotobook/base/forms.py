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

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'description', 'resize']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['name', 'original']   