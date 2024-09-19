from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100)
    organizer = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    max_participants = models.IntegerField(null=True, blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('registered', 'Registered'),
        ('attended', 'Attended'),
        ('cancelled', 'Cancelled')
    ])
    registration_date = models.DateTimeField(auto_now_add=True)
