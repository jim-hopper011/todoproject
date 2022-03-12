from .models import Task
from django import forms

class TaskF(forms.ModelForm):
    class Meta:
        model=Task
        fields= ['name', 'priority', 'date']