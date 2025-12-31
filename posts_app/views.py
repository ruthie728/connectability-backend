from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

from users_app.models import UserProfile
from follows_app.models import Follow
from notifications_app.models import Notification


# -------------------------
# Posts
# -------------------------
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content']
    ordering = ['-created_at']

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        serializer.save(user=user_profile)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


# -------------------------
# Comments
# -------------------------
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id']).order_by('-created_at')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        user_profile = UserProfile.objects.get(user=self.request.user)

        comment = serializer.save(user=user_profile, post=post)

        # 🔔 Comment notification (skip self)
        if post.user != user_profile:
            Notification.objects.create(
                sender=user_profile,
                receiver=post.user,
                notif_type='comment',
                post=post,
                comment=comment
            )


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


# -------------------------
# Likes
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

            # 🔔 Like notification (skip self)
            if post.user != user_profile:
                Notification.objects.create(
                    sender=user_profile,
                    receiver=post.user,
                    notif_type='like',
                    post=post
                )

        return Response({
            'liked': liked,
            'likes_count': post.likes.count()
        })


# -------------------------
# Feed
# -------------------------
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        following_ids = Follow.objects.filter(
            follower=user_profile
        ).values_list('following', flat=True)

        return Post.objects.filter(
            user__in=list(following_ids) + [user_profile]
        ).order_by('-created_at')