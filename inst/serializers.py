from rest_framework import serializers
from inst.models import Post, Like, Follow

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Follow
        fields = '__all__'
