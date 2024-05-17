from rest_framework import permissions

class IsCommunityAdmin(permissions.BasePermission):
    """
    Community admin permission
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if user is admin
        """
        return obj.admin == request.user