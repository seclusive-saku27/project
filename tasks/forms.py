# filepath: /C:/Users/abhis/Desktop/Assignment webknot/assignment/tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'deadline', 'status', 'assigned_attendee']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(choices=Task.STATUS_CHOICES),
            'assigned_attendee': forms.CheckboxSelectMultiple(),
        }