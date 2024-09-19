from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Group, GroupMembership
from .serializers import GroupSerializer, GroupMembershipSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        group = self.get_object()
        members = GroupMembership.objects.filter(group=group)
        serializer = GroupMembershipSerializer(members, many=True)
        return Response(serializer.data)

class GroupMembershipViewSet(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.all()
    serializer_class = GroupMembershipSerializer