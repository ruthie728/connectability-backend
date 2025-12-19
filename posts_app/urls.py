from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, LikeToggleView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='posts-list-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', CommentListCreateView.as_view(), name='post-comments'),
    path('<int:post_id>/like/', LikeToggleView.as_view(), name='post-like'),
]