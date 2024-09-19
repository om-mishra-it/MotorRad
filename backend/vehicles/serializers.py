from rest_framework import serializers
from .models import Vehicle, VehicleFeature, UserVehicleInteraction

class VehicleFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFeature
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    features = VehicleFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'
        extra_kwargs = {field.name: {'required': False} for field in Vehicle._meta.fields if field.name != 'id'}

class UserVehicleInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVehicleInteraction
        fields = '__all__'
        extra_kwargs = {
            'date_of_interaction': {'required': False},
            'location': {'required': False},
            'duration': {'required': False},
            'rating': {'required': False},
            'review': {'required': False},
            'photos': {'required': False},
        }
