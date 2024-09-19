from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, UserPreference, UserConnection, UserAchievement
from .serializers import UserSerializer, UserPreferenceSerializer, UserConnectionSerializer, UserAchievementSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']

    @action(detail=True, methods=['post'])
    def set_profile_picture(self, request, pk=None):
        user = self.get_object()
        if 'profile_picture' in request.data:
            user.profile_picture = request.data['profile_picture']
            user.save()
            return Response({'status': 'profile picture set'})
        else:
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)

class UserPreferenceViewSet(viewsets.ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

class UserConnectionViewSet(viewsets.ModelViewSet):
    queryset = UserConnection.objects.all()
    serializer_class = UserConnectionSerializer

    @action(detail=False, methods=['get'])
    def my_connections(self, request):
        connections = UserConnection.objects.filter(user=request.user)
        serializer = self.get_serializer(connections, many=True)
        return Response(serializer.data)

class UserAchievementViewSet(viewsets.ModelViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = UserAchievementSerializer