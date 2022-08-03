from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'text','price','capacity','photo', 'important', 'completed']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }