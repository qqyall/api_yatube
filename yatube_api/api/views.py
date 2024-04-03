from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from posts.models import Comment, Group, Post

from .mixins import UpdateDestroyMixin
from .serializers import CommentSerializer, GroupSerializer, PostSerializer

Users = get_user_model()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PostViewSet(UpdateDestroyMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        username = get_object_or_404(Users, pk=self.request.user.id)
        serializer.save(author=username)


class CommentViewSet(UpdateDestroyMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        username = get_object_or_404(Users, pk=self.request.user.id)
        serializer.save(post=post, author=username)
