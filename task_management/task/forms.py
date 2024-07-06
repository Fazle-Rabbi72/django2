from django import forms
from .models import TaskModel
from category.forms import TaskCategory

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = TaskModel
        fields = '__all__'
