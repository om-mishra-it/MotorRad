from django.db import models

class Notification(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    notification_type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
