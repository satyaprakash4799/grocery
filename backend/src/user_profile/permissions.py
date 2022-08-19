from rest_framework.permissions import BasePermission

from .models import BlackListedToken

class IsTokenValid(BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        is_allowed_user = True
        token = (request.auth.token).decode('utf8')
        try:
            is_blacklisted = BlackListedToken.objects.get(user=user_id, token=token)
            if is_blacklisted:
                is_allowed_user = False
        except BlackListedToken.DoesNotExist:
            is_allowed_user = True
        return is_allowed_user

class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        isNotAuthenticated = True
        if request.user and request.user.is_authenticated:
            isNotAuthenticated = False
        return isNotAuthenticated