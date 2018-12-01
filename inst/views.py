from inst.models import Post, Like, Follow
from inst.serializers import PostSerializer, LikeSerializer, FollowSerializer
from rest_framework import viewsets

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_queryset(self):
        queryset = Post.objects.all()
        username = self.request.query_params.get('user', None)
        if username is not None:
            queryset = queryset.filter(author=username)
        return queryset

class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = Like.objects.all()
        username = self.request.query_params.get('user', None)
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset

class FollowView(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self):
        queryset = Follow.objects.all()
        username = self.request.query_params.get('user', None)
        if username is not None:
            queryset = queryset.filter(follower=username)
        return queryset
