from rest_framework.exceptions import NotFound
from rest_framework.permissions import BasePermission

class IsStaffOr404(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True 
        raise NotFound()
