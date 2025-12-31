from rest_framework import serializers
from .models import Follow
from users_app.models import UserProfile
from users_app.serializers import UserSerializer

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']

    def get_follower(self, obj):
        return UserSerializer(obj.follower.user).data

    def get_following(self, obj):
        return UserSerializer(obj.following.user).data