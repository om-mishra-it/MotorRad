from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    reputation_score = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    # Make the default User model fields optional
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
    key = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)

class UserConnection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connections')
    connected_user = models.ForeignKey(User, on_delete=models.CASCADE)
    connection_type = models.CharField(max_length=20, choices=[('friend', 'Friend'), ('follower', 'Follower')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('blocked', 'Blocked')])
    created_at = models.DateTimeField(auto_now_add=True)

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_earned = models.DateTimeField(auto_now_add=True)
    badge_url = models.URLField(blank=True, null=True)