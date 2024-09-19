from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)

class GroupMembership(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, default='member', choices=[
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('member', 'Member')
    ])
    joined_at = models.DateTimeField(auto_now_add=True)