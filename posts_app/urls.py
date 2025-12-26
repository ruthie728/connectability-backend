from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    LikeToggleView,
    FeedView
)

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('', PostListCreateView.as_view(), name='posts-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('<int:post_id>/like/', LikeToggleView.as_view(), name='post-like'),
]