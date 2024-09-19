from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.viewsets import UserViewSet, UserPreferenceViewSet, UserConnectionViewSet, UserAchievementViewSet
from vehicles.viewsets import VehicleViewSet, VehicleFeatureViewSet, UserVehicleInteractionViewSet
from social.viewsets import PostViewSet, CommentViewSet, LikeViewSet, TagViewSet, TaggableItemViewSet
from groups.viewsets import GroupViewSet, GroupMembershipViewSet
from events.viewsets import EventViewSet, EventParticipantViewSet
from notifications.viewsets import NotificationViewSet
from activity_logs.viewsets import UserActivityLogViewSet

router = DefaultRouter()

# Users app
router.register(r'users', UserViewSet)
router.register(r'user-preferences', UserPreferenceViewSet)
router.register(r'user-connections', UserConnectionViewSet)
router.register(r'user-achievements', UserAchievementViewSet)

# Vehicles app
router.register(r'vehicles', VehicleViewSet)
router.register(r'vehicle-features', VehicleFeatureViewSet)
router.register(r'user-vehicle-interactions', UserVehicleInteractionViewSet)

# Social app
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'tags', TagViewSet)
router.register(r'taggable-items', TaggableItemViewSet)

# Groups app
router.register(r'groups', GroupViewSet)
router.register(r'group-memberships', GroupMembershipViewSet)

# Events app
router.register(r'events', EventViewSet)
router.register(r'event-participants', EventParticipantViewSet)

# Notifications app
router.register(r'notifications', NotificationViewSet)

# Activity Logs app
router.register(r'activity-logs', UserActivityLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]