from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи'
        }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание задачи',
                'rows': 5,
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            })
        }
