# filepath: /C:/Users/abhis/Desktop/Assignment webknot/assignment/tasks/models.py
from django.db import models
from attendee.models import Attendee

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    assigned_attendee = models.ManyToManyField(Attendee, related_name='assigned_tasks', blank=True)

    def __str__(self):
        return self.name