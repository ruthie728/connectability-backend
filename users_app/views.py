from rest_framework import generics, permissions, filters
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer
from notifications_app.models import Notification
from follows_app.models import Follow


# -------------------------
# Registration API
# -------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


# -------------------------
# Login API
# -------------------------
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username})
        return Response({'error': 'Invalid Credentials'}, status=400)


# -------------------------
# User Search API
# -------------------------
class UserSearchView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'bio', 'country']


# -------------------------
# Follow Toggle (with Notification)
# -------------------------
class FollowToggleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        follower_profile = UserProfile.objects.get(user=request.user)
        following_profile = UserProfile.objects.get(user=target_user)

        follow, created = Follow.objects.get_or_create(
            follower=follower_profile,
            following=following_profile
        )

        if not created:
            follow.delete()
            return Response({'status': 'unfollowed'})

        # Create notification for follow
        Notification.objects.create(
            sender=follower_profile,
            receiver=following_profile,
            notif_type='follow'
        )

        return Response({'status': 'followed'})