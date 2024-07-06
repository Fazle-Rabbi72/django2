from typing import Any
from django import forms
from django.core import validators

# without validation form

class contactForm(forms.Form):
    name = forms.CharField(label="User Name", help_text="Total length must be 20 characters", widget=forms.TextInput(attrs={'placeholder': "Enter your name...."}))

    email=forms.EmailField(label="User Eamil",widget=forms.TextInput(attrs={'placeholder': "Enter your email...."}))
    file=forms.FileField()
    age=forms.IntegerField()
    weight=forms.FloatField()
    blance=forms.DecimalField()
    check=forms.BooleanField()
    Birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','small'),('M','medium'),('L','large')]
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL=[('M','Masrum'),('P','Papperoni'),('S','Sos')]
    pizza=forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)

# validation form

# class stForm(forms.Form):
#     name = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'placeholder': "Enter your name...."}))
#     email=forms.EmailField(label="User Eamil",widget=forms.TextInput(attrs={'placeholder': "Enter your email...."}))

    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter at least 10 chararceter")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Email must contain .com")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = cleaned_data.get('name')
    #     valemail = cleaned_data.get('email')

    #     if valname and len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")

    #     if valemail and '.com' not in valemail:
    #         raise forms.ValidationError("Your email must contain '.com'")
      
# bulit in validator in django
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")
class stForm(forms.Form):
    name =forms.CharField(
        validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    
    email =forms.CharField(
        widget=forms.EmailInput,
        validators=[validators.EmailValidator(message="Enter a valid Email")])
    
    age = forms.IntegerField(
        validators=[validators.MaxValueValidator(34, message="age must be maximum 34"),
                    validators.MinValueValidator(24, message="age must be at least 24")])
    
    file = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message = '.pdf .png Only')])
    
    text = forms.CharField(
        widget=forms.TextInput, validators=[len_check])

class passwordvaliditionForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput,help_text="Password must be 8 character")
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data= super().clean()
        valpass=self.cleaned_data['password']
        valconpass=self.cleaned_data['confirm_password']
        valnam=self.cleaned_data['name']
        if len(valnam)<15:
            raise forms.ValidationError("Enter name with at least 15 character")
        if len(valpass)!=8:
            raise forms.ValidationError("Please enter password with 8 character")
        if len(valconpass)!=8:
            raise forms.ValidationError("Please enter confirm password with 8 character")
        if valpass!=valconpass:
            raise forms.ValidationError("password dosen't match")

        