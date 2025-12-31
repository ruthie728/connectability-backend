from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Follow
from notifications_app.models import Notification
from users_app.models import UserProfile

class FollowToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = User.objects.get(id=user_id)

        # Prevent self-follow
        if target_user == request.user:
            return Response({"detail": "You cannot follow yourself"}, status=400)

        follower_profile = UserProfile.objects.get(user=request.user)
        following_profile = UserProfile.objects.get(user=target_user)

        follow, created = Follow.objects.get_or_create(
            follower=follower_profile,
            following=following_profile
        )

        if not created:
            follow.delete()
            return Response({'status': 'unfollowed'})

        # Create notification ONLY when following
        Notification.objects.create(
            sender=follower_profile,
            receiver=following_profile,
            notif_type='follow'
        )

        return Response({'status': 'followed'})