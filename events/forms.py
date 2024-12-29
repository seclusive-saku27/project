from django import forms
from .models import Event
from django.contrib.auth.models import User
from .models import Profile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date', 'attendees']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'datetimepicker-input', 'data-target': '#datetimepicker1'}),
            'attendees': forms.CheckboxSelectMultiple(),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'})
        }