from rest_framework import serializers
from .models import User, UserPreference, UserConnection, UserAchievement

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio', 'location', 'reputation_score', 'is_verified')
        extra_kwargs = {
            'email': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'profile_picture': {'required': False},
            'bio': {'required': False},
            'location': {'required': False},
        }

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'

class UserConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConnection
        fields = '__all__'

class UserAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAchievement
        fields = '__all__'