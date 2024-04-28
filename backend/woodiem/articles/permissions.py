from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 읽기 작업은 모든 사용자에게 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 작업은 객체의 소유자에게만 허용
        return obj.author == request.user
