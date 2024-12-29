# filepath: /C:/Users/abhis/Desktop/Assignment webknot/assignment/events/models.py
from django.db import models
from attendee.models import Attendee
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(Attendee, related_name='event_attendees', blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

