from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from users_app.models import UserProfile
from follows_app.models import Follow


# -------------------------
# List & create posts
# -------------------------
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(author=user_profile)


# -------------------------
# Retrieve, update, delete a single post
# -------------------------
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


# -------------------------
# List & create comments for a post
# -------------------------
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(author=user_profile, post=post)


# -------------------------
# Toggle like for a post
# -------------------------
class LikeToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user_profile = UserProfile.objects.get(user=request.user)

        if user_profile in post.likes.all():
            post.likes.remove(user_profile)
            liked = False
        else:
            post.likes.add(user_profile)
            liked = True

        return Response({
            'liked': liked,
            'likes_count': post.likes.count()
        })


# -------------------------
# User Feed (posts from followed users + own posts)
# -------------------------
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)

        following_profiles = Follow.objects.filter(
            follower=user_profile
        ).values_list('following', flat=True)

        return Post.objects.filter(
            author__in=list(following_profiles) + [user_profile]
        ).order_by('-created_at')