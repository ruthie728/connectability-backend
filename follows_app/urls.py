from django.urls import path
from .views import FollowToggleView

urlpatterns = [
    path('<int:user_id>/toggle/', FollowToggleView.as_view(), name='follow-toggle'),
]