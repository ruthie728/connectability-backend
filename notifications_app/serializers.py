from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.user.username', read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'sender',
            'notif_type',
            'post',
            'comment',
            'read',
            'created_at'
        ]