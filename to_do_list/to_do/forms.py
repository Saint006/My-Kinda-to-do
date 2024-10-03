from django.forms import ModelForm
from . models import Todolist

class TaskForm(ModelForm):
    class Meta:
        model = Todolist
        fields = '__all__'