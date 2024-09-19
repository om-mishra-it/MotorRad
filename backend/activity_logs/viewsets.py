from rest_framework import viewsets
from .models import UserActivityLog
from .serializers import UserActivityLogSerializer

class UserActivityLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer

    def get_queryset(self):
        return UserActivityLog.objects.filter(user=self.request.user)