from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vehicle, VehicleFeature, UserVehicleInteraction
from .serializers import VehicleSerializer, VehicleFeatureSerializer, UserVehicleInteractionSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'manufacturer', 'category', 'type']

    @action(detail=True, methods=['get'])
    def features(self, request, pk=None):
        vehicle = self.get_object()
        features = VehicleFeature.objects.filter(vehicle=vehicle)
        serializer = VehicleFeatureSerializer(features, many=True)
        return Response(serializer.data)

class VehicleFeatureViewSet(viewsets.ModelViewSet):
    queryset = VehicleFeature.objects.all()
    serializer_class = VehicleFeatureSerializer

class UserVehicleInteractionViewSet(viewsets.ModelViewSet):
    queryset = UserVehicleInteraction.objects.all()
    serializer_class = UserVehicleInteractionSerializer

    @action(detail=False, methods=['get'])
    def my_interactions(self, request):
        interactions = UserVehicleInteraction.objects.filter(user=request.user)
        serializer = self.get_serializer(interactions, many=True)
        return Response(serializer.data)