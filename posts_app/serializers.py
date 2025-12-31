from rest_framework import serializers
from .models import Post, Comment
from users_app.serializers import UserSerializer

# -------------------------
# Comment Serializer
# -------------------------
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'created_at']


# -------------------------
# Post Serializer
# -------------------------
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'likes_count', 'comments']

    def get_likes_count(self, obj):
        return obj.likes.count()