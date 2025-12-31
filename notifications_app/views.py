from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer
from users_app.models import UserProfile

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile = UserProfile.objects.get(user=self.request.user)
        return Notification.objects.filter(receiver=profile)


class MarkNotificationReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        profile = UserProfile.objects.get(user=request.user)
        notification = Notification.objects.get(id=pk, receiver=profile)
        notification.read = True
        notification.save()
        return Response({"detail": "Notification marked as read"})