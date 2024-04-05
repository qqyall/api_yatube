from rest_framework import permissions


class CanUserGetDeleteUpdateObj(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # check if author is user, sended a request,
        # then he can do whatever he wants to object

        return obj.author == request.user
