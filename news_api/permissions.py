from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is tring to edit their own rofile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnNews(permissions.BasePermission):
    """Allow user to update their own news"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own news"""
        if request.method in permissions.SAFE_METHODS: # Allow list and retrieve for any
            return True

        return obj.author.id == request.user.id
