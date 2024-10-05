from django import forms
from django.forms import ModelForm
from .models import Todolist
from datetime import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = '__all__'
        widgets = {
            'deline': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

    def clean_deline(self):
        deline = self.cleaned_data.get('deline')
        if deline and isinstance(deline, str):
            try:
                # Convert string to datetime
                deline = datetime.fromisoformat(deline)
            except ValueError:
                raise forms.ValidationError("Invalid date format")
        return deline
