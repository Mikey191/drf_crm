from rest_framework import permissions


class IsOwnerOrStaff(permissions.BasePermission):
    """
    Разрешает доступ:
    - владельцу объекта (менеджеру)
    - или администратору/персоналу (is_staff)
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superadmin:
            return True
        return obj.manager == request.user
