from django.urls import path
from .views import RegisterView, LoginView, UserSearchView, FollowToggleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow-toggle'),
]