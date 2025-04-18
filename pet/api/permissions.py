from rest_framework import permissions


class AuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj.author
            or request.method in permissions.SAFE_METHODS
            or request.user.is_staff
        )
