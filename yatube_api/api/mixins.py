from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

Users = get_user_model()


class UpdateDestroyMixin(viewsets.ModelViewSet):
    def check_author(self, request):
        request_user = get_object_or_404(Users, username=request.user)
        post_author = self.get_object().author
        return post_author == request_user

    def update(self, request, *args, **kwargs):
        if self.check_author(request):
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if self.check_author(request):
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
