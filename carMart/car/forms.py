from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['name','email','body']
        widgets={
            'body':forms.Textarea(attrs={'row':3}),
            # 'is_completed':forms.BooleanInput()
        }