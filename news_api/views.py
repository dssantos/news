from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from news_api import serializers
from news_api import models
from news_api import permissions

        
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,  IsAuthenticated)

    def get_queryset(self):
        """restricts the returned profile to a given user, except if adminuser"""
        if self.request.user.is_staff:
            return models.UserProfile.objects.all()
        queryset = models.UserProfile.objects.filter(id=self.request.user.id)
        return queryset
