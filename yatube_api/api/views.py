from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from posts.models import Comment, Group, Post, User

from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from .permissions import CanUserGetDeleteUpdateObj


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CanUserGetDeleteUpdateObj, IsAuthenticated, )

    def perform_create(self, serializer):
        username = get_object_or_404(User, pk=self.request.user.id)
        serializer.save(author=username)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CanUserGetDeleteUpdateObj, IsAuthenticated, )

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        username = get_object_or_404(User, pk=self.request.user.id)
        serializer.save(post=post, author=username)
