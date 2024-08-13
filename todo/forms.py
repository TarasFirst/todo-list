from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags', 'is_done']
        widgets = {
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            'deadline': forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            'tags': forms.SelectMultiple(attrs={"class": "form-control"}),
            'is_done': forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
        }
