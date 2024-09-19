from django.db import models

class UserActivityLog(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    activity_details = models.JSONField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
