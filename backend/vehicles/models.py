from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    year_of_manufacture = models.IntegerField(null=True, blank=True)
    engine_type = models.CharField(max_length=50, blank=True, null=True)
    fuel_type = models.CharField(max_length=50, blank=True, null=True)
    horsepower = models.IntegerField(null=True, blank=True)
    top_speed = models.FloatField(null=True, blank=True)
    seating_capacity = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    wheelbase = models.FloatField(null=True, blank=True)
    ground_clearance = models.FloatField(null=True, blank=True)
    cargo_capacity = models.FloatField(null=True, blank=True)
    fuel_efficiency = models.FloatField(null=True, blank=True)
    emission_standard = models.CharField(max_length=20, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

class VehicleFeature(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)
    is_standard = models.BooleanField(default=True)

class UserVehicleInteraction(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=20, choices=[
        ('driven', 'Driven'),
        ('experienced', 'Experienced'),
        ('seen', 'Seen'),
        ('want_to_try', 'Want to Try')
    ])
    date_of_interaction = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    duration = models.DurationField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(blank=True, null=True)
    photos = models.JSONField(default=list, blank=True, null=True)
    visibility = models.CharField(max_length=20, default='public', choices=[
        ('public', 'Public'),
        ('friends', 'Friends'),
        ('private', 'Private')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)