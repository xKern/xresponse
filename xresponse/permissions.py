from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    message = 'This resource requires authentication'
    code = 810

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
