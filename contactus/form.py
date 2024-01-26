from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from .models import Register


class Contactus(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":
                                                           'form-control form', "id": "emailinput", "placeholder": 'Email Address'

                                                           }))

    uplaod_img = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "form-control", "type": "file", "name": 'files'
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form", "placeholder": "full name", "name": 'fullname'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control form", "placeholder": "username", "name": 'username'

    }))

    class Meta:
        model = Register
        fields = '__all__'
