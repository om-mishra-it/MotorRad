from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    media_urls = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=20, default='public', choices=[
        ('public', 'Public'),
        ('friends', 'Friends'),
        ('private', 'Private')
    ])
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    likes_count = models.IntegerField(default=0)

class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class TaggableItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)
