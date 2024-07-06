from django import forms
from django.core import validators
from first_app.models import StudentModel
import datetime

# without validation form
class contactForm(forms.Form):
    name = forms.CharField(
        label="User Name", help_text="Total length must be at least 10 characters", widget=forms.TextInput(attrs={'placeholder': "Enter your name...."}),validators=[validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')]                      
    )

    email =forms.CharField(
        label="User Email",widget=forms.TextInput(attrs={'placeholder':"Enter your email...."}),
        validators=[validators.EmailValidator(message="Enter a valid Email address")])

    age = forms.IntegerField(
        help_text="Age must be 18 to 60 years",label="User Age",
        validators=[validators.MaxValueValidator(60, message="age must be maximum 60"),
                    validators.MinValueValidator(18, message="age must be at least 18")])

    weight=forms.FloatField(
        help_text="Age must be 45 to 60 years",label="User weight",
        validators=[validators.MaxValueValidator(60, message="age must be maximum 60"),
                    validators.MinValueValidator(45, message="age must be at least 45")]
    )

    blance=forms.DecimalField()

    check=forms.BooleanField()

    day = forms.DateField(initial=datetime.date.today)

    Birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    appointment=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))


    CHOICESS=[('I','ICT'),('E','ENGLISH'),('T','TEXTILE'),('C','CIVIL')]
    Department=forms.MultipleChoiceField(choices=CHOICESS,widget=forms.CheckboxSelectMultiple)

    CHOICES=[('D','Day'),('E','Evining')]
    Batch=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    Favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        widgets = {
            'date_field': forms.DateInput(attrs={'type': 'date'}),
            'date_time_field':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }