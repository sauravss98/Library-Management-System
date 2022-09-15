
from rest_framework.permissions import BasePermission
from django.conf import settings
from User.models import UserData

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.usertype==UserData.Users.ADMIN)