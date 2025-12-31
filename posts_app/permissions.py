from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to allow only owners to edit or delete objects.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE METHODS = GET, HEAD, OPTIONS
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.author == request.user