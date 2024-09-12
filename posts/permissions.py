from rest_framework import permissions


class PostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list", "retrieve"]:
            return True

        if view.action in ["create", "update", "partial_update", "destroy"]:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user.id == request.user.id
