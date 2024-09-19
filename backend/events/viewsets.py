from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event, EventParticipant
from .serializers import EventSerializer, EventParticipantSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'event_type']

    @action(detail=True, methods=['get'])
    def participants(self, request, pk=None):
        event = self.get_object()
        participants = EventParticipant.objects.filter(event=event)
        serializer = EventParticipantSerializer(participants, many=True)
        return Response(serializer.data)

class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer