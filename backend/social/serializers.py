from rest_framework import serializers
from .models import Post, Comment, Like, Tag, TaggableItem

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'content': {'required': False},
            'media_urls': {'required': False},
        }

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TaggableItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggableItem
        fields = '__all__'