from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms


class RegistretionFrom(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'requird'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'requird'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class UserChangeData(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']