from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Follow
from users_app.models import UserProfile
from django.shortcuts import get_object_or_404

class FollowToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # Get the target user's profile
        target_profile = get_object_or_404(UserProfile, user__id=user_id)
        # Get the requesting user's profile
        user_profile = request.user.userprofile

        # Check if follow already exists
        follow, created = Follow.objects.get_or_create(follower=user_profile, following=target_profile)
        if not created:
            follow.delete()
            return Response({'status': 'unfollowed'})
        return Response({'status': 'followed'})