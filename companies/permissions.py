from rest_framework.permissions import BasePermission, SAFE_METHODS

class CompanyPermission(BasePermission):
    """
    POST и GET доступны всем авторизованным.
    PUT/PATCH/DELETE — только админам.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.is_admin()