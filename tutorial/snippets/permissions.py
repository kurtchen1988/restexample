from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
    # 修改权限，只让一个snippet的拥有者才能修改
        if request.method in permissions.SAFE_METHODS:
        # 所有的读取方法都会被允许，包括GET, HEAD和OPTIONS
            return True

        # 只允许snippet的拥有者
        return obj.owner == request.user