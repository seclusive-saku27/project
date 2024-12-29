# filepath: /C:/Users/abhis/Desktop/Assignment webknot/assignment/attendee/models.py
from django.db import models

class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField('events.Event', related_name='attendee_events', blank=True)
    tasks = models.ManyToManyField('tasks.Task', related_name='assigned_tasks', blank=True)

    def __str__(self):
        return self.name